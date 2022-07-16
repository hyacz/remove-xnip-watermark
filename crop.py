#!/usr/bin/python3
# coding=utf-8
# author: hyacz<hyacz@foxmail.com>
# 2018-05-30 18:42
# 

import io
import pasteboard
from PIL import Image

# define
WM_H   = 40

img_bytes = io.BytesIO()
pb        = pasteboard.Pasteboard()

# get image
img       = Image.open(io.BytesIO(pb.get_contents(pasteboard.PNG)))

# if retina display
dpi = img.info.get('dpi', (96, 96))
if dpi[0] > 96:
    WM_H *= 2

# if too narrow
if img.width <= 400:
    exit()

# crop
img.crop((0, WM_H, img.width, img.height)).save(img_bytes, format='PNG', dpi=dpi)

# set cilpboard
pb.set_contents(img_bytes.getvalue(), type=pasteboard.PNG)