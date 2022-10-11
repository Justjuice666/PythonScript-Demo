# *_* coding : UTF-8 *-*
# 开发人员  : JustJuice
# 开发时间  : 2022/10/3  20:03
# 文件名称  : pornhubVideo.py
# 开发工具  ：PyCharm
import time

from requests import get
from re import compile, S
from os import popen, remove
from selenium import webdriver
from json import loads
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'referer': 'https://cn.pornhub.com/',
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()


def get_info(video_url):
    browser.get(video_url)
    html = browser.page_source
    pattern = compile('id="player".*?<script type="text/javascript">(.*?)playerObjList', S)
    js = pattern.findall(html)[0]
    js = js + "\nconsole.log(media_5)"
    with open('js.js', mode='w', encoding='utf8') as f:
        f.write(js)
    cmd = "node js.js"
    download_url = popen(cmd).read()
    remove('js.js')
    return download_url


def download_video(video_url):
    print("下载中，请稍等：")
    string = """
    ua=620eeaccf0f03dc51ea5a9f1f3fb4360; platform=pc; bs=150k615u2aaow1fnxycbu9myqd7y8qea; ss=199768980049837153; fg_fcf2e67d6468e8e1072596aead761f2b=1666.100000; fg_79a480e053a843252802a2ca03a36825=59066.100000; atatusScript=hide; _gid=GA1.2.164861908.1664930622; _gat=1; _ga_B39RFFWGYY=GS1.1.1664930622.1.0.1664930622.0.0.0; _ga=GA1.1.1506019011.1664930622; d_fs=1; d_uidb=20e1fe2b-5e95-a028-0a24-92c3a373f7d5; d_uid=20e1fe2b-5e95-a028-0a24-92c3a373f7d5; _hjSessionUser_1180136=eyJpZCI6IjdkZGMzYWI1LWRjNjUtNTEyYi1hY2NlLWU3NzAxMTc1MmQwZiIsImNyZWF0ZWQiOjE2NjQ5MzA2MjI4NTcsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_1180136=eyJpZCI6IjFiMDdkZTQ5LWNhZDEtNDNjNi1hMzI1LTU4MWEwMjJlYzg0MyIsImNyZWF0ZWQiOjE2NjQ5MzA2MjM5NDksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0
    """
    cookies = {}
    for line in string.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    resp = get(video_url, headers=headers)
    with open("{}.mp4".format('name'), mode="wb") as f:
        f.write(resp.content)
    # print(cookies)
    # resp = get(video_url, headers=headers)
    # with open("{}.mp4".format('name'), mode="wb") as f:
    #     for chunk in resp.iter_content(chunk_size=1024 * 1024):
    #         f.write(chunk)
    print('下载完毕')


def main():
    url = input('请输入网址：')
    download_url = get_info(url)
    browser.get(download_url)
    html = browser.page_source
    cookie = browser.get_cookies()
    print(cookie)
    # 关闭浏览器
    browser.close()
    pattern = compile('pre-wrap;">(.*)</pre>', S)
    urls_json = pattern.findall(html)[0].replace('&amp;', '&')
    urls_list = loads(str(urls_json))
    for i in range(len(urls_list)):
        print(' {}.'.format(i + 1), urls_list[i]['quality'])
    num = input('请输入想要下载的视频的清晰度的序号：')
    video_url = urls_list[int(num) - 1]['videoUrl']
    print(video_url)
    download_video(video_url)


if __name__ == '__main__':
    main()
