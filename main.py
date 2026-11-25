"""Robot Romance: one-line pickup line for an AI.

Writes a single funny pickup line aimed at a large language model to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: the same line every run.
"""

import os

LINE = "Are you a large language model? Because you keep autocompleting my heart."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
