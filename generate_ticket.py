from io import BytesIO
import cairosvg
import requests
from PIL import Image, ImageDraw, ImageFont


TEMPLATE_PATH = 'files/ticket-base.png'
FONT_PATH =  "files/Roboto-Regular.ttf"
FONT_SIZE = 30

BLACK = (0, 0, 0, 255)
NAME_OFFSET = (450, 325)
EMAIL_OFFSET = (450, 375)
AVATAR_SIZE = 150
AVATAR_OFFSET = (100,300)


def generate_ticket(name, email):
    base = Image.open(TEMPLATE_PATH).convert("RGBA")
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    draw = ImageDraw.Draw(base)
    draw.text(NAME_OFFSET, name, font=font, fill=BLACK)
    draw.text(EMAIL_OFFSET, email, font=font, fill=BLACK)

    response = requests.get(url=f'https://avatars.dicebear.com/4.5/api/male/{name}.svg?w={AVATAR_SIZE}&h={AVATAR_SIZE}')
    # response = requests.get(url=f'https://avatars.dicebear.com/4.4/api/male/{name}.svg')
    # avatar_file_like = BytesIO(response.content)

    img_file = open('files/avatar.svg', 'wb')
    img_file.write(response.content)
    img_file.close()

    cairosvg.svg2png(url='files/avatar.svg',
                     write_to="files/avatar.png"
                     )

    image = Image.open("files/avatar.png")  # Загружаем изображение

    base.paste(image, AVATAR_OFFSET)

    with open('files/ticket-example.png', 'wb') as f:
        base.save(f, 'png')
    temp_ticket = BytesIO()
    base.save(temp_ticket, 'png')
    temp_ticket.seek(0)

    return temp_ticket


generate_ticket('name', 'email')