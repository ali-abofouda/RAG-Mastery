"""
Centralized Configuration & Environment Loader for RAG Mastery.

Handles project path resolution, environment variable loading (.env),
and defensive guards against Windows Smart App Control blocked binaries.
"""

import os
import sys
from pathlib import Path
from typing import Optional


def get_project_root() -> Path:
    """Resolve project root directory reliably across notebooks and modules."""
    current = Path(__file__).resolve().parent.parent
    return current


def load_rag_environment(env_file: Optional[str] = None) -> Path:
    """Load .env file and apply system safety guards for Windows Smart App Control.

    Returns:
        Path to the project root directory.
    """
    root = get_project_root()

    # 1. Apply safety guard against blocked native DLLs under Windows SAC
    for blocked_module in ("torch", "sentence_transformers", "spacy"):
        if blocked_module not in sys.modules:
            sys.modules[blocked_module] = None

    # 2. Ensure project root is present in sys.path
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    # 3. Load environment variables
    from dotenv import load_dotenv

    target_env = Path(env_file) if env_file else (root / ".env")
    if target_env.exists():
        load_dotenv(target_env)

    return root
