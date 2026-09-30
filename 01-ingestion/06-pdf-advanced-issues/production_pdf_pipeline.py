"""
Robust Text-Based PDF Processing Pipeline for RAG Systems
=========================================================
Architectural Refactor based on Enterprise Review:
1. Modular Architecture: Decoupled into specialized single-responsibility classes:
   - TextNormalizer (Ligatures, Smart De-hyphenation, Non-destructive Arabic)
   - HeaderFooterDetector (Margin-only line matching, NO substring contamination)
   - MetadataManager (Document SHA-256 ID, Global sequential indexing)
   - ChunkDeduplicator (Configurable tracking without silent data loss)
2. Smart De-hyphenation: Preserves legitimate compound words (e.g. 'well-known', 'state-of-the-art').
3. Non-destructive Arabic: Original text is preserved for LLM generation; normalized text stored for search.
4. Document ID: Unique 16-char SHA-256 hash derived from file binary bytes.
5. Accurate Scope: Focused on robust text extraction (Level 2 Text Foundation).
"""

import hashlib
import logging
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Configure structured logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("RobustTextPDFPipeline")


# =============================================================================
# 1. Text Normalization Component
# =============================================================================
class TextNormalizer:
    """
    Handles typographic ligatures, smart de-hyphenation, and non-destructive Arabic processing.
    """
    LIGATURES_MAP = {
        "ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl", "ﬆ": "st",
    }

    # Common English hyphenated prefixes and compound words that should KEEP their hyphen
    HYPHENATED_PRESERVE_PREFIXES = {
        "self", "well", "co", "pre", "post", "non", "anti", "multi", "cross", "state", "user", "real"
    }

    ARABIC_TASHKEEL = re.compile(r"[\u0617-\u061A\u064B-\u0652]")

    def __init__(self, preserve_original_arabic: bool = True):
        self.preserve_original_arabic = preserve_original_arabic

    def normalize_ligatures(self, text: str) -> str:
        """Replace typographic ligatures with standard ASCII equivalents."""
        for lig, rep in self.LIGATURES_MAP.items():
            text = text.replace(lig, rep)
        return text

    def smart_de_hyphenate(self, text: str) -> str:
        """
        Merges words broken across line breaks, BUT preserves legitimate compound words.
        Example:
          'artifi-\\ncial' -> 'artificial'
          'well-\\nknown'  -> 'well-known' (preserved!)
        """
        def replace_match(match: re.Match) -> str:
            w1 = match.group(1)
            w2 = match.group(2)
            # If the first word is a common compound prefix, preserve the hyphen
            if w1.lower() in self.HYPHENATED_PRESERVE_PREFIXES:
                return f"{w1}-{w2}"
            return f"{w1}{w2}"

        return re.sub(r"(\b[a-zA-Z]+)-\n([a-zA-Z]+\b)", replace_match, text)

    def normalize_arabic_for_search(self, text: str, normalize_taa_marbuta: bool = False) -> str:
        """
        Create a normalized copy of Arabic text specifically for search/retrieval indexing.
        Safe defaults:
        - Strip Tashkeel & Tatweel
        - Unify Alef variants (إ أ آ ا -> ا)
        - Unify Yaa / Alef Maqsura (ي ى -> ي)
        - Taa Marbuta is PRESERVED by default (to avoid semantic drift like مدرسة -> مدرسه)
        """
        text = self.ARABIC_TASHKEEL.sub("", text)  # Strip Tashkeel
        text = text.replace("\u0640", "")          # Strip Tatweel
        text = re.sub("[إأآا]", "ا", text)         # Unify Alef variants
        text = re.sub("[يى]", "ي", text)           # Unify Yaa / Alef Maqsura
        if normalize_taa_marbuta:
            text = re.sub("[ةه]", "ه", text)
        return text

    def clean_text(self, text: str) -> Tuple[str, Optional[str]]:
        """
        Cleans text and returns a tuple of (clean_original_text, normalized_search_text).
        """
        # 1. Ligatures
        text = self.normalize_ligatures(text)
        # 2. Smart De-hyphenation
        text = self.smart_de_hyphenate(text)

        # 3. Standardize whitespace without destroying paragraph structure
        lines = [line.strip() for line in text.splitlines()]
        cleaned_lines = []
        last_blank = False
        for line in lines:
            if not line:
                if not last_blank:
                    cleaned_lines.append("")
                    last_blank = True
            else:
                cleaned_lines.append(line)
                last_blank = False
        cleaned_text = "\n".join(cleaned_lines).strip()

        # 4. Arabic handling (Non-destructive)
        search_text = None
        if re.search(r"[\u0600-\u06FF]", cleaned_text):
            search_text = self.normalize_arabic_for_search(cleaned_text)

        return cleaned_text, search_text


# =============================================================================
# 2. Safe Header & Footer Removal Component
# =============================================================================
class HeaderFooterFilter:
    """
    Detects and strips recurring headers and footers safely.
    Crucial fix: Only matches exact lines at the top 2 and bottom 2 margins of pages.
    Never uses blind `replace()` which corrupts inner text.
    """
    def __init__(self, frequency_threshold: float = 0.70, min_line_length: int = 4):
        self.frequency_threshold = frequency_threshold
        self.min_line_length = min_line_length

    def detect_recurring_lines(self, pages: List[Document]) -> Tuple[Set[str], Set[str]]:
        if len(pages) < 3:
            return set(), set()

        top_candidates = []
        bottom_candidates = []

        for doc in pages:
            lines = [l.strip() for l in doc.page_content.splitlines() if l.strip()]
            if lines:
                # Top 2 margin lines
                top_candidates.extend(lines[:2])
                # Bottom 2 margin lines
                bottom_candidates.extend(lines[-2:])

        threshold_count = int(len(pages) * self.frequency_threshold)

        recurring_top = {
            line for line, cnt in Counter(top_candidates).items()
            if cnt >= threshold_count and len(line) >= self.min_line_length
        }
        recurring_bottom = {
            line for line, cnt in Counter(bottom_candidates).items()
            if cnt >= threshold_count and len(line) >= self.min_line_length
        }

        return recurring_top, recurring_bottom

    def strip_headers_footers(self, text: str, recurring_top: Set[str], recurring_bottom: Set[str]) -> str:
        """Safely removes recurring lines ONLY if they appear at the top or bottom margins."""
        lines = text.splitlines()
        if not lines:
            return text

        # Strip from top
        start_idx = 0
        while start_idx < len(lines) and lines[start_idx].strip() in recurring_top:
            start_idx += 1

        # Strip from bottom
        end_idx = len(lines)
        while end_idx > start_idx and lines[end_idx - 1].strip() in recurring_bottom:
            end_idx -= 1

        return "\n".join(lines[start_idx:end_idx]).strip()


# =============================================================================
# 3. Metadata & Document Identity Component
# =============================================================================
class MetadataManager:
    """
    Generates deterministic Document IDs, globally sequential chunk indexing, and rich provenance.
    """
    @staticmethod
    def generate_document_id(file_path: Path) -> str:
        """Generate a deterministic 16-character SHA-256 hash of the binary file."""
        return hashlib.sha256(file_path.read_bytes()).hexdigest()[:16]

    @staticmethod
    def create_chunk_metadata(
        doc_id: str,
        file_path: Path,
        page_number: int,
        total_pages: int,
        page_chunk_idx: int,
        global_chunk_idx: int,
        chunk_text: str,
        search_text: Optional[str] = None,
    ) -> Dict:
        content_hash = hashlib.sha256(chunk_text.strip().encode("utf-8")).hexdigest()
        meta = {
            "document_id": doc_id,
            "source_file": file_path.name,
            "page_number": page_number,
            "total_pages": total_pages,
            "chunk_id": f"{doc_id[:8]}_p{page_number:02d}_c{page_chunk_idx:02d}",
            "global_chunk_index": global_chunk_idx,
            "char_count": len(chunk_text),
            "content_hash": content_hash[:12],
            "has_arabic": bool(re.search(r"[\u0600-\u06FF]", chunk_text)),
        }
        if search_text:
            meta["normalized_search_preview"] = search_text[:100]
        return meta


# =============================================================================
# 4. Master Pipeline: RobustTextPDFPipeline
# =============================================================================
class RobustTextPDFPipeline:
    """
    Robust Text-Based PDF Pipeline for Level 2 RAG implementations.
    Orchestrates Normalization, Header/Footer filtering, Recursive Splitting, and Metadata Management.
    """
    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 50,
        min_page_char_length: int = 40,
        header_footer_threshold: float = 0.70,
        enable_deduplication: bool = True,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.min_page_char_length = min_page_char_length
        self.enable_deduplication = enable_deduplication

        self.normalizer = TextNormalizer()
        self.hf_filter = HeaderFooterFilter(frequency_threshold=header_footer_threshold)
        self.meta_manager = MetadataManager()
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", ". ", " ", ""],
        )

    def process(self, pdf_path: str) -> List[Document]:
        file_path = Path(pdf_path)
        if not file_path.exists():
            raise FileNotFoundError(f"PDF file not found at: {pdf_path}")

        logger.info(f"Starting robust parsing for: {file_path.name}")
        doc_id = self.meta_manager.generate_document_id(file_path)
        logger.info(f"Generated Document ID: {doc_id}")

        # 1. Load raw pages
        loader = PyPDFLoader(str(file_path))
        raw_pages = loader.load()
        total_pages = len(raw_pages)

        # 2. Detect recurring header/footer candidates at margins
        rec_top, rec_bottom = self.hf_filter.detect_recurring_lines(raw_pages)
        if rec_top or rec_bottom:
            logger.info(f"Detected recurring margin lines: Top={rec_top}, Bottom={rec_bottom}")

        # 3. Clean pages & filter empty ones
        cleaned_pages_data: List[Tuple[int, str, Optional[str]]] = []

        for idx, page in enumerate(raw_pages, start=1):
            raw_text = page.page_content

            # Safe margin-only header/footer stripping
            stripped_text = self.hf_filter.strip_headers_footers(raw_text, rec_top, rec_bottom)

            # Clean and normalize
            cleaned_text, search_text = self.normalizer.clean_text(stripped_text)

            # Skip blank / low-content pages
            if len(cleaned_text) < self.min_page_char_length:
                logger.info(f"Skipping page #{idx} (content length {len(cleaned_text)} < threshold {self.min_page_char_length})")
                continue

            cleaned_pages_data.append((idx, cleaned_text, search_text))

        # 4. Split and enrich chunks
        final_chunks: List[Document] = []
        seen_hashes: Set[str] = set()
        global_chunk_idx = 0

        for page_num, clean_content, search_content in cleaned_pages_data:
            chunks = self.splitter.split_text(clean_content)

            for page_chunk_idx, chunk_text in enumerate(chunks, start=1):
                content_hash = hashlib.sha256(chunk_text.strip().encode("utf-8")).hexdigest()

                if self.enable_deduplication and content_hash in seen_hashes:
                    logger.info(f"Deduplication: skipped identical chunk on page {page_num}")
                    continue

                seen_hashes.add(content_hash)
                global_chunk_idx += 1

                # Generate chunk-specific normalized search representation if Arabic text exists
                chunk_search_text = (
                    self.normalizer.normalize_arabic_for_search(chunk_text)
                    if re.search(r"[\u0600-\u06FF]", chunk_text)
                    else None
                )

                metadata = self.meta_manager.create_chunk_metadata(
                    doc_id=doc_id,
                    file_path=file_path,
                    page_number=page_num,
                    total_pages=total_pages,
                    page_chunk_idx=page_chunk_idx,
                    global_chunk_idx=global_chunk_idx,
                    chunk_text=chunk_text,
                    search_text=chunk_search_text,
                )

                final_chunks.append(Document(page_content=chunk_text, metadata=metadata))

        logger.info(f"Pipeline finished: Generated {len(final_chunks)} chunks for {file_path.name}")
        return final_chunks


# =============================================================================
# Self-Test Execution
# =============================================================================
if __name__ == "__main__":
    # Resolve path to centralized root data directory
    root_data_pdf = Path(__file__).resolve().parents[2] / "data" / "pdf" / "sample_financial_report.pdf"
    sample_pdf = root_data_pdf if root_data_pdf.exists() else Path("data/pdf/sample_financial_report.pdf")

    if not sample_pdf.exists():
        print(f"Sample PDF not found at {sample_pdf}.")
    else:
        pipeline = RobustTextPDFPipeline(
            chunk_size=300,
            chunk_overlap=40,
            min_page_char_length=40,
        )
        chunks = pipeline.process(str(sample_pdf))

        print(f"\n[+] Processing Completed Successfully!")
        print(f"[+] Total Cleaned & Enriched Chunks: {len(chunks)}\n")

        for chunk in chunks:
            m = chunk.metadata
            print(f"--- Global Index #{m['global_chunk_index']} | ID: {m['chunk_id']} ---")
            print(f"Doc ID: {m['document_id']} | Page: {m['page_number']}/{m['total_pages']} | Chars: {m['char_count']}")
            print(f"Content:\n{chunk.page_content[:140]}...")
            print()
