# *_* coding : UTF-8 *-*
# 开发人员  : JustJuice
# 开发时间  : 2022/9/30  17:25
# 文件名称  : webp2gif.py
# 开发工具  ：PyCharm

"""
for the webpFolder:
    webp to gif in GifFolder
"""

from PIL import Image
import os
from os import path

webpFolder = 'D:/2gif/webp'
gifFolder = 'D:/2gif/gif'

for i, j, filenames in os.walk(webpFolder):
    for filename in filenames:
        im = Image.open(path.join(webpFolder, filename))
        gifName = filename.replace('webp', 'gif')
        im.save(path.join(gifFolder, gifName), 'gif', save_all=True, background=0)
