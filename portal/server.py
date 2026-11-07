"""
RAG-Mastery Learning Portal Server
High-performance local web server powering the interactive documentation reader.
Always serves fresh content directly from docs/ on every request.
"""

import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

PORTAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = PORTAL_DIR.parent
DOCS_DIR = REPO_ROOT / "docs"

# Fallback stage labels in case README is missing
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
    """Extract clean H1 title or first meaningful header from markdown."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s.startswith("# "):
                    title = s[2:].strip()
                    # Clean markdown links or bold tags from title
                    title = title.replace("**", "").replace("__", "")
                    return title
                if s.startswith("### "):
                    return s[4:].strip().replace("**", "")
    except Exception:
        pass
    
    stem = filepath.stem
    if stem.lower() == "readme":
        return "نظرة عامة ودليل المرحلة"
    return stem.replace("-", " ").title()

def get_stage_title(stage_dir: Path) -> str:
    """Extract stage title from stage README or fallback mapping."""
    readme = stage_dir / "README.md"
    if readme.exists():
        t = extract_markdown_title(readme)
        if t and len(t) > 3 and not t.startswith("نظرة عامة"):
            return t
    return STAGE_FALLBACKS.get(stage_dir.name, stage_dir.name.replace("-", " ").title())

def get_docs_tree():
    """Dynamically scan docs/ to guarantee real-time synchronization with added files."""
    tree = []
    
    # Root Overview
    root_readme = DOCS_DIR / "README.md"
    if root_readme.exists():
        try:
            content = root_readme.read_text(encoding="utf-8")
            words = len(content.split())
        except Exception:
            words = 500
        tree.append({
            "stage_id": "root",
            "stage_title": "خارطة المنهج الشاملة (Overview)",
            "docs": [{
                "title": "دليل المسار الشامل وخارطة الـ 191 محاضرة",
                "rel_path": "README.md",
                "filename": "README.md",
                "reading_time_min": max(1, round(words / 180))
            }]
        })
    
    for stage_dir in sorted(DOCS_DIR.iterdir()):
        if not stage_dir.is_dir() or stage_dir.name.startswith("."):
            continue
            
        stage_key = stage_dir.name
        stage_title = get_stage_title(stage_dir)
        
        stage_docs = []
        for file in sorted(stage_dir.glob("*.md")):
            rel_path = f"{stage_key}/{file.name}"
            try:
                content = file.read_text(encoding="utf-8")
                words = len(content.split())
                reading_time = max(1, round(words / 180))
            except Exception:
                reading_time = 3
                
            title = extract_markdown_title(file)
            stage_docs.append({
                "title": title,
                "rel_path": rel_path,
                "filename": file.name,
                "reading_time_min": reading_time
            })
            
        if stage_docs:
            # Place README first, then sort naturally by lecture numbers
            stage_docs.sort(key=lambda d: (0 if d["filename"] == "README.md" else 1, d["filename"]))
            tree.append({
                "stage_id": stage_key,
                "stage_title": stage_title,
                "docs": stage_docs
            })
            
    return tree

def search_docs(query: str):
    """Full-text keyword search across all markdown documents."""
    query = query.strip().lower()
    if not query:
        return []
        
    results = []
    for file in sorted(DOCS_DIR.rglob("*.md")):
        rel_path = file.relative_to(DOCS_DIR).as_posix()
        try:
            content = file.read_text(encoding="utf-8")
        except Exception:
            continue
            
        lines = content.splitlines()
        file_title = extract_markdown_title(file)
        
        matches = []
        for i, line in enumerate(lines):
            if query in line.lower():
                clean_line = line.strip().replace("#", "").replace("*", "")
                if clean_line:
                    matches.append(clean_line[:180])
                if len(matches) >= 3:
                    break
                    
        if matches:
            results.append({
                "rel_path": rel_path,
                "title": file_title,
                "matches": matches
            })
            
    return results

class PortalRequestHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        # Serve SPA index
        if path == "/" or path == "/index.html":
            index_file = PORTAL_DIR / "index.html"
            if index_file.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(index_file.read_bytes())
            else:
                self.send_error(404, "index.html not found")
            return

        # Serve static assets in portal directory (if any)
        static_file = (PORTAL_DIR / path.lstrip("/")).resolve()
        if static_file.exists() and static_file.is_file() and str(static_file).startswith(str(PORTAL_DIR)):
            content_type = "application/octet-stream"
            if static_file.suffix == ".json":
                content_type = "application/json; charset=utf-8"
            elif static_file.suffix == ".css":
                content_type = "text/css; charset=utf-8"
            elif static_file.suffix == ".js":
                content_type = "application/javascript; charset=utf-8"
            elif static_file.suffix in [".png", ".jpg", ".svg", ".webp"]:
                content_type = f"image/{static_file.suffix.lstrip('.')}"
                
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            self.wfile.write(static_file.read_bytes())
            return

        # Real-time docs tree API (Live synchronization)
        if path == "/api/tree":
            tree = get_docs_tree()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(tree, ensure_ascii=False).encode("utf-8"))
            return

        # Real-time single document reader API (Live synchronization)
        if path == "/api/doc":
            rel_path = params.get("path", [""])[0]
            if not rel_path:
                self.send_error(400, "Missing path parameter")
                return

            target_file = (DOCS_DIR / rel_path).resolve()
            if not str(target_file).startswith(str(DOCS_DIR.resolve())) or not target_file.exists():
                self.send_error(404, "Document not found")
                return

            try:
                content = target_file.read_text(encoding="utf-8")
                title = extract_markdown_title(target_file)
                response = {
                    "rel_path": rel_path,
                    "title": title,
                    "content": content
                }
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self.send_error(500, f"Error reading document: {e}")
            return

        # Real-time search API
        if path == "/api/search":
            q = params.get("q", [""])[0]
            results = search_docs(q)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(results, ensure_ascii=False).encode("utf-8"))
            return

        self.send_error(404, "Endpoint not found")

def run(port: int = 8080):
    server_address = ("", port)
    httpd = HTTPServer(server_address, PortalRequestHandler)
    print(f"RAG-Mastery Learning Portal running at http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run(p)
