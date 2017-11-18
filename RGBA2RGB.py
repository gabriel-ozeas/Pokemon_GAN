from PIL import Image
import os

src = "./resizeData"
dst = "./resizeBlack"

if not os.path.exists(dst):
    os.mkdir(dst)

for each in os.listdir(src):
    png = Image.open(os.path.join(src, each))

    if png.mode == 'RGBA':
        png.load()
        background = Image.new("RGB", png.size, (0,0,0))
        background.paste(png, mask = png.split()[3])
        background.convert('RGB').save(os.path.join(dst, each.split('.')[0] + '.jpeg'), 'JPEG')
    else:
        png.convert('RGB').save(os.path.join(dst, each.split('.')[0] + '.jpeg'), 'JPEG')

