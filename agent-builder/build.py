#!/usr/bin/env python3
"""
AGENTS.md Builder - Quick Start Script
Usage: python build.py
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from simple_builder import main

if __name__ == "__main__":
    print("\n🚀 Starting AGENTS.md Builder...\n")
    main()