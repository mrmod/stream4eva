from PIL import Image
import numpy as np
import sys
import io
from random import randint
from time import sleep

# Create an image and draw some chaning shapes
# and colors on it. Make your own screen saver!
def create_image(origin=(0,0), bw=128, bh=128):
    w, h = 512, 512
    RGB = 3
    mat = np.zeros((h, w, RGB), dtype=np.uint8)

    origin_x = randint(0, 255)
    origin_y = randint(0, 255)
    origin_x = 40
    origin_y = 50
    color = [
        randint(128, 254),
        randint(128, 254),
        randint(128, 254),
    ]

    box_w = randint(128, 255)
    box_h = randint(128, 255)

    print(f"X[{origin[0]}:{origin[0] + bw}] Y[{origin[1]}:{origin[1] + bh}]", file=sys.stderr)
    mat[
        origin[0]:origin[0]+bw,
        origin[1]:origin[1]+bh
    ] = color

    return Image.fromarray(mat, 'RGB')

# Genrate images and write them to stdout
# ffmpeg can use image2pipe to receive them
def generate_images(stream=False):
    x, y, w, h = 0, 0, 128, 128
    # Instead of outsize, the (x,y) position
    # could be #OfSiteVisitors % 256
    outsize = True
    while True:
        image = create_image(
            (x, y), w, h
        )
        # write out PNG stream on STDOUT
        image.save(sys.stdout.buffer, "png")

        sleep(1/25)
        if outsize:
            x += 1
            y += 1
        else:
            x -= 1
            y -= 1
        if x == 256 or y == 256:
            x = 256
            y = 256
            outsize = False
        if x == 0 or y == 0:
            x = 0
            y = 0
            outsize = True
        

if __name__ == "__main__":
    try:
        generate_images(stream=sys.argv[1])
    except Exception:
        generate_images()
