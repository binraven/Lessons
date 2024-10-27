from pprint import pprint

from PIL import Image
import requests

Image.effect_mandelbrot((512, 512), (-3, -2.5, 2, 2.5), 100).show()


with Image.open("pic1.png") as im:
    rotate = im.rotate(45)
    rotate.show()
    rotate.save("pic2.png")

with Image.open("pic1.png") as im:
    im = im.convert("L")
    im.show()


r = requests.get('http://urban-university.pro/auth')

print(r.url)
print(r.status_code)
print(r.history)
r1 = requests.get('https://urban-university.pro/')
pprint(r1.content)

