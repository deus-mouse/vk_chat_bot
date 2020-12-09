import cairo
# import rsvg
import requests
import cairosvg
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


# работает! скачивает svg, и сохраняет локально
# img = requests.get("https://avatars.dicebear.com/4.4/api/male/deusmouse.svg")
# img_file = open('files/avatar5.svg', 'wb')
# img_file.write(img.content)
# img_file.close()
#
# работает! берет картинку локально и конвертирует сохраняет локально
# cairosvg.svg2png(url='files/avatar5.svg',
#                  write_to="files/avatar11.png"
#                  )

response = requests.get(url='https://avatars.dicebear.com/4.4/api/male/deusmouse.svg')
img_file = open('files/avatar.svg', 'wb')
img_file.write(response.content)
img_file.close()

cairosvg.svg2png(url='files/avatar.svg',
                 write_to="files/avatar.png"
                 )

image = Image.open("files/avatar.png")  # Загружаем изображение

avatar = Image.open(avatar_file_like)


# response_svg = requests.get('https://avatars.dicebear.com/4.4/api/male/deusmouse.svg')
# print(response_svg.content)
# cairosvg.svg2png(url=response_svg.content,
#                  write_to="files/avatar12.png"
#                  )
# cairosvg.svg2png(url=response_svg,
#                  write_to="files/avatar3.png"
#                  )
# cairosvg.svg2png(url=f'{response}',
#                  write_to="files/avatar6.png"
#                  )
#


