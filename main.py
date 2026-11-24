"""Two Lines to Your Past Self — make.fun entry.

Writes one two-line warning to $MAKEFUN_OUTPUT_DIR/entry.txt:
line 1 warns the past self about one specific moment in a single
sentence; line 2 says in one sentence why that moment mattered and
what changed because of it. Pure stdlib, deterministic, no network.
"""

import os

LINE_1 = (
    "Don't send that 2:14 a.m. text from the taxi outside her place "
    "— it starts 'we need to talk', you mean it as a joke, she reads "
    "it as the end."
)

LINE_2 = (
    "That text cost you the only person who laughed at your worst "
    "jokes, and losing her taught you to sleep on a feeling before "
    "you speak."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    text = LINE_1 + "\n" + LINE_2 + "\n"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
