"""
Build static distribution for RAG-Mastery Learning Portal on GitHub Pages.
Generates a pre-bundled docs_data.json and builds a standalone static site.
"""

import os
import json
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
PORTAL_DIR = REPO_ROOT / "portal"
DIST_DIR = REPO_ROOT / "dist"

STAGE_FALLBACKS = {
    "00-rag-fundamentals": "00 - أساسيات ومفاهيم الـ RAG",
    "01-ingestion": "01 - استيعاب ومعالجة المستندات (Data Ingestion)",
    "02-vector-embeddings": "02 - تضمينات المتجهات وفضاء المعنى (Vector Embeddings)",
    "03-vector-stores-and-databases": "03 - فهارس وقواعد بيانات المتجهات (Vector Stores & DBs)",
    "04-advanced-chunking": "04 - تقنيات التقطيع الدلالي المتقدم (Advanced Chunking)",
    "05-hybrid-search-and-retrieval": "05 - البحث الهجين وإعادة الترتيب (Hybrid Search & Reranking)",
    "06-query-enhancement": "06 - تحسين وتوسيع الاستعلامات (Query Enhancement)",
    "07-multimodal-rag": "07 - أنظمة RAG متعددة الوسائط (Multimodal RAG)",
    "08-langchain-and-langgraph": "08 - أطر عمل LangChain و LangGraph",
    "09-agentic-rag": "09 - وكلاء الذكاء الاصطناعي المستقلة (Agentic RAG)",
    "10-self-correcting-rag": "10 - أنظمة RAG ذاتية التصحيح (Self-Correcting RAG)",
    "11-evaluation-and-benchmarking": "11 - التقييم والمقاييس المرجعية (Evaluation & RAGAS)",
    "12-fine-tuning-vs-rag": "12 - الضبط الدقيق مقابل الـ RAG (Fine-Tuning vs RAG)",
    "13-caching-and-cost-optimization": "13 - التخزين المؤقت وخفض التكاليف (Caching & Cost)",
    "14-enterprise-security-governance": "14 - أمن البيانات والحوكمة المؤسسية (Security & Governance)",
    "15-production-deployment-mlops": "15 - النشر والعمليات الإنتاجية (Production MLOps)",
    "16-capstone-enterprise-agents": "16 - المشروع الشامل للشركات (Capstone Project)",
}

def extract_markdown_title(filepath: Path) -> str:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith("# "):
                    return stripped[2:].strip().replace("**", "")
                if stripped.startswith("### "):
                    return stripped[4:].strip().replace("**", "")
    except Exception:
        pass
    name = filepath.stem
    if name == "README":
        return "دليل ونظرة عامة على المرحلة"
    return name.replace("-", " ").title()

def get_stage_title(stage_dir: Path) -> str:
    readme = stage_dir / "README.md"
    if readme.exists():
        t = extract_markdown_title(readme)
        if t and len(t) > 3 and not t.startswith("دليل ونظرة"):
            return t
    return STAGE_FALLBACKS.get(stage_dir.name, stage_dir.name.replace("-", " ").title())

def build_static_bundle():
    """Create static data bundle containing tree and full content of all docs."""
    tree = []
    docs_map = {}
    
    # 1. Root README
    root_readme = DOCS_DIR / "README.md"
    if root_readme.exists():
        content = root_readme.read_text(encoding="utf-8")
        title = extract_markdown_title(root_readme)
        tree.append({
            "stage_id": "root",
            "stage_title": "خارطة المنهج الشاملة (Overview)",
            "docs": [{
                "title": title,
                "rel_path": "README.md",
                "filename": "README.md",
                "reading_time_min": max(1, round(len(content.split()) / 180))
            }]
        })
        docs_map["README.md"] = {
            "rel_path": "README.md",
            "title": title,
            "content": content
        }

    # 2. Stage directories
    for stage_dir in sorted(DOCS_DIR.iterdir()):
        if not stage_dir.is_dir() or stage_dir.name.startswith("."):
            continue
            
        stage_key = stage_dir.name
        stage_title = get_stage_title(stage_dir)
        stage_docs = []
        
        for file in sorted(stage_dir.glob("*.md")):
            rel_path = f"{stage_key}/{file.name}"
            content = file.read_text(encoding="utf-8")
            title = extract_markdown_title(file)
            reading_time = max(1, round(len(content.split()) / 180))
            
            stage_docs.append({
                "title": title,
                "rel_path": rel_path,
                "filename": file.name,
                "reading_time_min": reading_time
            })
            
            docs_map[rel_path] = {
                "rel_path": rel_path,
                "title": title,
                "content": content
            }
            
        if stage_docs:
            stage_docs.sort(key=lambda d: (0 if d["filename"] == "README.md" else 1, d["filename"]))
            tree.append({
                "stage_id": stage_key,
                "stage_title": stage_title,
                "docs": stage_docs
            })

    bundle = {
        "tree": tree,
        "docs": docs_map
    }
    
    # Clean output dist directory
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save bundle into dist and portal
    bundle_json_text = json.dumps(bundle, ensure_ascii=False, indent=2)
    (DIST_DIR / "docs_bundle.json").write_text(bundle_json_text, encoding="utf-8")
    (PORTAL_DIR / "docs_bundle.json").write_text(bundle_json_text, encoding="utf-8")
    
    # Copy index.html to dist
    shutil.copy(PORTAL_DIR / "index.html", DIST_DIR / "index.html")
    
    # Create .nojekyll for GitHub Pages
    (DIST_DIR / ".nojekyll").touch()
    
    print(f"Static site built successfully in {DIST_DIR} with {len(docs_map)} documents!")

if __name__ == "__main__":
    build_static_bundle()
