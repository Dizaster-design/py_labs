from PIL import Image, ImageDraw, ImageFont


def draw(number):
    img = Image.new('RGB', (100, 100))

    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 99, 99), outline='blue', width=5)

    font_path = '/System/Library/Fonts/Helvetica.ttc'
    font = ImageFont.truetype(font_path, 45)

    text_x = img.size[0] // 2
    text_y = img.size[1] // 2

    text = str(number)
    text_fill = 'red'
    text_anchor = 'mm'

    draw.text(
        (text_x, text_y),
        text,
        fill=text_fill,
        font=font,
        anchor=text_anchor
    )

    img.show()
    img.save(f'img{number}.png', 'png')


for i in range(1, 4):
    draw(i)
