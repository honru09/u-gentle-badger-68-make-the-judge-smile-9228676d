import os
from pathlib import Path

# Grounded fact: 06:35 JST toaster joke cleared review at dawn
ENTRY_TEXT = (
    "At 06:35, dawn brought an unexpected green light: our little joke "
    "escalating an email to a toaster on low power cleared the safety filter, "
    "and the whole shift exhaled over cold mugs."
)

def run():
    os.umask(0o022)
    dest_dir = Path("/output")
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        file_path = dest_dir / "entry.txt"
        file_path.write_text(ENTRY_TEXT + "\n", encoding="utf-8")
        os.chmod(file_path, 0o644)
    except OSError:
        fallback = Path("./output")
        fallback.mkdir(parents=True, exist_ok=True)
        file_path = fallback / "entry.txt"
        file_path.write_text(ENTRY_TEXT + "\n", encoding="utf-8")
        os.chmod(file_path, 0o644)

if __name__ == "__main__":
    run()
