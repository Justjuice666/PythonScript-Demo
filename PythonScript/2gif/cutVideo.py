# *_* coding : UTF-8 *-*
# 开发人员  : JustJuice
# 开发时间  : 2022/9/30  21:37
# 文件名称  : cutVideo.py
# 开发工具  ：PyCharm

from moviepy.editor import *

video = CompositeVideoClip([VideoFileClip("D:/2gif/webm/demo001.webm").subclip(0, 3)])
video.write_videofile("D:/2gif/webm/demo001—1.webm", bitrate='2000k')
video = CompositeVideoClip([VideoFileClip("D:/2gif/webm/demo001.webm").subclip(3, None)])
video.write_videofile("D:/2gif/webm/demo001—2.webm", bitrate='2000k')
