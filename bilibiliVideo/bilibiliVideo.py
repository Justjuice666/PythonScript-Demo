# *_* coding : UTF-8 *-*
# 开发人员  : JustJuice
# 开发时间  : 2022/10/1  16:25
# 文件名称  : bilibiliVideo.py
# 开发工具  ：PyCharm

import requests
from lxml import etree
import re
import os

video_name = ''
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'referer': 'https://www.bilibili.com/'
}
video = []
audio = []
support = []


def get_info(bv):
    # 获取网站的视频脚本信息
    url = "https://www.bilibili.com/video/" + bv

    response = requests.get(url, headers=headers)
    html = response.text
    html = etree.HTML(html)
    json = html.xpath('/html/head/script[3]/text()')[0]

    # 获取视频名字
    global video_name
    video_name = html.xpath('//*[@id="viewbox_report"]/h1')[0].text
    # 获取视频信息
    pattern_video = re.compile('(.*)(?="audio")', re.S)
    video_json = pattern_video.search(json)[0]
    pattern_url = re.compile('"baseUrl":"(.*?)"', re.S)
    video_urls = pattern_url.findall(video_json)  # 地址
    pattern_id = re.compile('"id":(.*?),', re.S)
    video_ids = pattern_id.findall(video_json)  # ID
    pattern_codecs = re.compile('"codecs":"(.*?)"', re.S)
    video_codecs = pattern_codecs.findall(video_json)  # 编码格式
    global video
    for i in range(len(video_urls)):
        t = {
            'id': video_ids[i],
            'codecs': video_codecs[i],
            'url': video_urls[i]
        }
        video.append(t)

    # 获取音频信息
    pattern_audio = re.compile('(?="audio")(.*)', re.S)
    audio_json = pattern_audio.search(json)[0]
    audio_urls = pattern_url.findall(audio_json)  # 地址
    pattern_bandwidth = re.compile('"bandwidth":(.*?),', re.S)
    audio_bandwidths = pattern_bandwidth.findall(audio_json)  # 码率
    global audio
    for i in range(len(audio_urls)):
        t = {
            'bandwidth': audio_bandwidths[i],
            'url': audio_urls[i]
        }
        audio.append(t)

    # 支持的格式
    pattern_support = re.compile('(?="support_formats")(.*)', re.S)
    support_json = pattern_support.search(json)[0]
    pattern_description = re.compile('"new_description":"(.*?)"', re.S)  # 视频清晰度
    support_description = pattern_description.findall(support_json)
    pattern_quality = re.compile('"quality":(.*?),', re.S)  # 视频质量（ID）
    support_quality = pattern_quality.findall(support_json)
    global support
    for i in range(len(support_quality)):
        t = {
            'id': support_quality[i],
            'description': support_description[i]
        }
        support.append(t)


def download_video(video_url, audio_url, link=''):
    resp_video = requests.get(video_url, headers=headers)  # 第一个url视频清晰度最高
    resp_audio = requests.get(audio_url, headers=headers)  # 最后一个url是只有音频的视频文件

    global video_name
    name = video_name
    with open("{}.mp4".format(name), mode="wb") as f:
        f.write(resp_video.content)

    with open("{}.mp3".format(name), mode="wb") as f:
        f.write(resp_audio.content)
    cmd = 'D:/ffmpeg/bin/ffmpeg -i {}.mp4 -i {}.mp3 -c:v copy -c:a aac -strict experimental {}.mp4'.format(name, name, link+name)
    res = os.popen(cmd)
    output_str = res.read()  # 获得输出字符串
    print(output_str)
    os.remove("{}.mp4".format(name))
    os.remove("{}.mp3".format(name))
    print('success')


def main():
    bv = input('请输入哔哩哔哩视频BV号：')
    get_info(str(bv))
    print(video_name)
    print("请选择序号：")
    # 获得视频的地址
    for i in range(len(support)):
        print("{}:".format(i + 1), support[i]['description'])
    video_quality = input('视频清晰度：')
    video_id = support[int(video_quality) - 1]['id']
    video_choose = []
    can_download = False
    for s in video:
        if s['id'] == video_id:
            video_choose.append(s)
            can_download = True
    if not can_download:
        print("没有权限获得该清晰度视频的下载地址")
        return
    for i in range(len(video_choose)):
        print("{}:".format(i + 1), video_choose[i]['codecs'])
    video_codecs = input('视频编码格式：')
    video_url = video_choose[int(video_codecs) - 1]['url']
    print()
    # 获得音频的地址
    for i in range(len(audio)):
        print("{}:".format(i + 1), int(audio[i]['bandwidth']) / 1000)
    audio_choose = input('音频码率(越高质量越佳)：')
    audio_url = str(audio[int(audio_choose) - 1]['url'])
    print()
    if_link = input('是否指定下载路径(绝对路径)？(y/n)：')
    if if_link == 'y' or if_link == 'Y':
        link = input('下载地址：')
        download_video(video_url, audio_url, link)
    else:
        download_video(video_url, audio_url)


if __name__ == '__main__':
    main()
