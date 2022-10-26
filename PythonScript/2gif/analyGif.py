# *_* coding : UTF-8 *-*
# 开发人员  : JustJuice
# 开发时间  : 2022/9/30  19:24
# 文件名称  : analyGif.py
# 开发工具  ：PyCharm
"""
save all frames in gif
count the number of the frames
"""
from PIL import Image
count = 0
im = Image.open('demo001.gif')
try:
    # im.save('picframe{:02d}.png'.format(im.tell()))
    count += 1
    while True:
        im.seek(im.tell() + 1)
        # im.save('picframe{:02d}.png'.format(im.tell()))
        count += 1
except:
    print("处理结束")

print(count)
