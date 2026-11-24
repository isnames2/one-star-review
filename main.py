# One-star review of gravity: deadpan, one line, 112 characters.
# The review is fixed text: no network, no randomness, same bytes every run.
import os
from pathlib import Path

REVIEW = "One star. Gravity holds the whole planet together but cannot be trusted with a single mug on the edge of a desk."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    Path(out_dir, "entry.txt").write_text(REVIEW, encoding="utf-8")

if __name__ == "__main__":
    main()
