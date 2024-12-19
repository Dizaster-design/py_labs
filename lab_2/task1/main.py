from PIL import Image

filename = "image.jpg"
with Image.open(filename) as img:
    img.load()

red, green, blue = img.split()
zeroed_band = blue.point(lambda _:0)

red_merge = Image.merge("RGB" , (red, zeroed_band, zeroed_band))
green_merge = Image.merge("RGB" , ( zeroed_band, green, zeroed_band))
blue_merge = Image.merge("RGB" , (zeroed_band, zeroed_band, blue))

img.show()
red_merge.show()
green_merge.show()
blue_merge.show()

