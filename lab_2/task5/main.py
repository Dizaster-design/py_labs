from PIL import Image
import os
import sys

params = dict(zip(sys.argv[1::2], sys.argv[2::2]))
filetype = params.get("--ftype")

if not filetype:
    raise ValueError("No --ftype parameter")

for filename in os.listdir("."):
    if filename.endswith(f".{filetype}"):
        with Image.open(filename) as img:
            img.resize((50, 50)).show()
