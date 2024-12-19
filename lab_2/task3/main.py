from PIL import Image, ImageFilter

image = "image.jpg"
logo = "logo.jpg"

with Image.open(image) as img, Image.open(logo) as logo:
    img.load()
    logo.load()

logo = logo.convert("L")
logo = logo.point(lambda x: 255 if x > 50 else 0)
logo = logo.resize(
    (logo.width // 2, logo.height // 2)
)

logo = logo.filter(ImageFilter.CONTOUR)
logo = logo.point(lambda x: 0 if x == 255 else 255)
logo = logo.crop((10, 10, logo.width - 10, logo.height - 10))
img.paste(logo, (0, 0), logo)
img.show()
img.save('image_with_watermark.jpg')