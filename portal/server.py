"""
RAG-Mastery Learning Portal Server
Zero-dependency local web server powering the interactive docs reader.
"""

import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

# Resolve base directories
PORTAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = PORTAL_DIR.parent
DOCS_DIR = REPO_ROOT / "docs"

STAGE_TITLES = {
    "00-rag-fundamentals": "00 - أساسيات ومفاهيم الـ RAG",
    "01-ingestion": "01 - استيعاب ومعالجة المستندات (Data Ingestion)",
    "02-vector-embeddings": "02 - تضمينات المتجهات وفضاء المعنى (Vector Embeddings)",
    "03-vector-stores-and-databases": "03 - فهارس وقواعد بيانات المتجهات (Vector Stores & DBs)",
    "04-advanced-chunking": "04 - تقنيات التقطيع الدلالي المتقدم (Advanced Chunking)",
    "05-hybrid-search-and-retrieval": "05 - البحث الهجين وإعادة الترتيب (Hybrid Search & Reranking)",
}

def extract_markdown_title(filepath: Path) -> str:
    """Extract first H1 title from markdown file, fallback to filename."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith("# "):
                    return stripped[2:].strip()
                if stripped.startswith("### "):
                    return stripped[4:].strip()
    except Exception:
        pass
    # Clean filename fallback
    name = filepath.stem
    if name == "README":
        return "دليل ونظرة عامة على المرحلة"
    return name.replace("-", " ").title()

def get_docs_tree():
    """Build a structured tree of all docs organized by stage and lectures."""
    tree = []
    
    # Root README
    root_readme = DOCS_DIR / "README.md"
    if root_readme.exists():
        tree.append({
            "stage_id": "root",
            "stage_title": "خارطة المنهج الشاملة (Overview)",
            "docs": [{
                "title": extract_markdown_title(root_readme),
                "rel_path": "README.md",
                "filename": "README.md",
                "reading_time_min": 5
            }]
        })
        
    for stage_dir in sorted(DOCS_DIR.iterdir()):
        if not stage_dir.is_dir() or stage_dir.name.startswith("."):
            continue
            
        stage_key = stage_dir.name
        stage_title = STAGE_TITLES.get(stage_key, stage_key.replace("-", " ").title())
        
        stage_docs = []
        for file in sorted(stage_dir.glob("*.md")):
            rel_path = f"{stage_key}/{file.name}"
            try:
                word_count = len(file.read_text(encoding="utf-8").split())
                reading_time = max(1, round(word_count / 180))
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
            # Place README first if present
            stage_docs.sort(key=lambda d: (0 if d["filename"] == "README.md" else 1, d["filename"]))
            tree.append({
                "stage_id": stage_key,
                "stage_title": stage_title,
                "docs": stage_docs
            })
            
    return tree

def search_docs(query: str):
    """Full-text search in all docs returning matching snippets."""
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
                # Extract surrounding context
                start = max(0, i - 1)
                end = min(len(lines), i + 2)
                snippet = " ... ".join([l.strip() for l in lines[start:end] if l.strip()])
                matches.append(snippet[:200])
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
        # Enable CORS and caching headers
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

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

        elif path == "/api/tree":
            tree = get_docs_tree()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(tree, ensure_ascii=False).encode("utf-8"))
            return

        elif path == "/api/doc":
            rel_path = params.get("path", [""])[0]
            if not rel_path:
                self.send_error(400, "Missing path parameter")
                return

            # Secure path traversal check
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

        elif path == "/api/search":
            q = params.get("q", [""])[0]
            results = search_docs(q)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(results, ensure_ascii=False).encode("utf-8"))
            return

        else:
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
