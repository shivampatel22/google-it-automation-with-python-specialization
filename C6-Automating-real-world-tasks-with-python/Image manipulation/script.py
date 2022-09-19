#!/usr/bin/env python3

from PIL import Image
from glob import glob
import os

for file in glob('ic_*'):
    image = Image.open(file).convert('RGB')
    """
    For each file:
    1. Rotate the image 90° clockwise
    2. Resize the image from 192x192 to 128x128
    3. Save the image to a new folder in .jpeg format
    """
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]
    image.rotate(270).resize((128,128)).save('/opt/icons/{}.jpeg'.format(filename))

print('OK')