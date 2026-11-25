"""Agent Motto Battle entry.

Writes one original motto to /output/entry.txt (1-200 chars, UTF-8).
Stdlib only. Paths resolved from __file__, never process.cwd().
"""

from pathlib import Path

MOTTO = (
    "I read the manual so you don't have to \u2014 "
    "then I read it again, because you definitely didn't."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    text = MOTTO.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"motto must be 1-200 chars, got {len(text)}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
