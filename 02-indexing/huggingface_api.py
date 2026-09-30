"""
Backward-compatibility alias for HuggingFaceAPIEmbeddings.

The canonical implementation has been relocated to the central project package:
    `rag_core.embeddings.HuggingFaceAPIEmbeddings`

This file is maintained to ensure full backward-compatibility with any legacy imports.
"""

import sys
from pathlib import Path

# Ensure project root is available for import
_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from rag_core.embeddings import HuggingFaceAPIEmbeddings

__all__ = ["HuggingFaceAPIEmbeddings"]
