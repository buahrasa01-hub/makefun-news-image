# make.fun news-image-01 entry: giant green NVIDIA logo + empty CEO chair,
# Jensen Huang stepped down (12 Nov 2026), Colette Kress interim CEO.
import os
import shutil

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry-news-nvidia.jpg")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(SOURCE, "rb") as src, open(OUTPUT, "wb") as dst:
        shutil.copyfileobj(src, dst)

if __name__ == "__main__":
    main()
