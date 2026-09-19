"""Allow `python -m quiz_cli`."""

from __future__ import annotations

import sys

from .quiz import main

if __name__ == "__main__":
    sys.exit(main())
