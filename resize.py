# resize pokeGAN.py
import os
import PIL
from PIL import Image

src = "./data"
dst = "./resizeData"
size = 256, 256

if not os.path.exists(dst):
    os.mkdir(dst)

for each in os.listdir(src):
    img = Image.open(os.path.join(src, each))
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(os.path.join(dst, each), "png")
    
