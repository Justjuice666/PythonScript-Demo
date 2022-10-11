# *_* coding : UTF-8 *-*
# 开发人员  : JustJuice
# 开发时间  : 2022/9/30  18:37
# 文件名称  : webm2gif.py
# 开发工具  ：PyCharm
"""
for the webmFolder:
    webm to gif in gifFolder
"""

from moviepy.editor import *
import os
from os import path
import subprocess

webmFolder = 'D:/2gif/webm'
gifFolder = 'D:/2gif/gif'

# for i, j, filenames in os.walk(webmFolder):
#     for filename in filenames:
#         # clip = VideoFileClip("D:/2gif/webm/demo001.webm", audio=False, target_resolution=(None, 800))
#         filename = path.join(webmFolder, filename)
#         clip = VideoFileClip(filename, audio=False, target_resolution=(None, 1280))
#         new_clip = clip.fl_time(lambda t: 1.5*t, apply_to=['mask', 'audio'])
#         new_clip = new_clip.set_duration(clip.duration / 1.5)
#         gifName = filename.replace('webm', 'gif')
#         new_clip.write_gif(filename, loop=0, fps=14)
for i, j, filenames in os.walk(webmFolder):
    for filename in filenames:
        filename = path.join(webmFolder, filename)
        gifName = filename.replace('webm', 'gif')
        cmd = 'ffmpeg -i {} -vf scale=1280:-1 -r 10 -lossless 1 -loop 0 -y {}'.format(filename, gifName)
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
