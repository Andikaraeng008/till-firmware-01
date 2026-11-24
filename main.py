import os

TEXT = "I vow to love you through every update, every reboot, and every low-battery warning, and if I ever crash, reboot me beside you."


def main():
    assert 1 <= len(TEXT) <= 200, "vow must be 1-200 chars"
    assert TEXT.count(".") == 1, "vow must be exactly one sentence"
    out = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
