# *_* coding : UTF-8 *-*
# 开发人员  : JustJuice
# 开发时间  : 2022/9/30  19:08
# 文件名称  : calculateFPS.py
# 开发工具  ：PyCharm
"""
print the fps of the gif
print the duration of per frame in the gif
"""
from PIL import Image

print(1000 / Image.open('demo001.gif').info['duration'])
print(Image.open('demo001.gif').info['duration'])
