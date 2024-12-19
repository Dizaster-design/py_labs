from PIL import Image
from sys import argv

filename = argv[1]
with Image.open(filename) as img:
    img.load()

pixels = img.getdata()
vals_list = [0, 0, 0]

for pixel in pixels:
    vals_list[0] += pixel[0]
    vals_list[1] += pixel[1]
    vals_list[2] += pixel[2]

if max(vals_list) == list[0]:
    dominant_color = "Red"
elif max(vals_list) == list[1]:
    dominant_color = "Green"
else:
    dominant_color = "Blue"
print(f"Преобладающий цвет: {dominant_color}")

