"""
Launcher script for RAG-Mastery Learning Portal.
Usage:
    python run_portal.py [port]
"""

import sys
import webbrowser
import threading
import time
from portal.server import run

def open_browser(port):
    time.sleep(1.0)
    url = f"http://localhost:{port}"
    print(f"Opening browser at: {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    
    # Open browser in a separate thread
    threading.Thread(target=open_browser, args=(port,), daemon=True).start()
    
    # Start web server
    run(port=port)
