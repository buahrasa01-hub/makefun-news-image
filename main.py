#!/usr/bin/env python3
"""Copy entry-news-nvidia.jpg to output path.
giant NVIDIA logo + empty CEO chair, Jensen Huang stepped down"""

import os
import shutil

def main():
    src = "entry-news-nvidia.jpg"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)

if __name__ == "__main__":
    main()
