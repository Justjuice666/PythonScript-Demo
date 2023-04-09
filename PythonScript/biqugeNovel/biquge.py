# *_* coding : UTF-8 *-*
# 开发人员  : JustJuice
# 开发时间  : 2023/4/9  14:49
# 文件名称  : biquge.py
# 开发工具  ：PyCharm

# import requests
import re
# from lxml import etree
# from bs4 import BeautifulSoup
# from pyquery import PyQuery as pq
#
# from requests import get
# from re import compile, S
# from os import popen, remove
from selenium import webdriver
# from json import loads
# import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'referer': 'https://www.beqege.com/',
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

txt = open('target.txt', mode='w+', encoding='utf8')


def get_one_page(url):
    browser.get(url)
    return browser.page_source


def parse_one_page(html):
    # 正则表达式
    pattern1 = re.compile(
        # '<a.*?<span.*?class="title">(.*?)</span>',
        '<h1>(.*?)</h1>',
        re.S
    )
    items1 = re.findall(pattern1, html)
    for item in items1:
        txt.write(item + '\n\n')
    pattern2 = re.compile(
        # '<a.*?<span.*?class="title">(.*?)</span>',
        '<p>(.*?)</p>',
        re.S
    )
    items2 = re.findall(pattern2, html)
    for item in items2:
        if item[0] == '【':
            continue
        if item == '本站所有小说为转载作品，所有章节均由网友上传，转载至本站只是为了宣传本书让更多读者欣赏。':
            continue
        if item == 'Copyright © 2015 笔趣阁 All Rights Reserved.':
            continue
        if item == '<a href="/sitemap/1.html">网站地图</a>':
            continue
        txt.write('  ' + item + '\n')
    txt.write('\n')

    # BeautifulSoup
    # soup = BeautifulSoup(html, 'lxml')
    # 方法选择器
    # items = soup.find_all(attrs={'class': 'hd'})
    # for item in items:
    #     movie_top_250.append(item.find(attrs={'class': 'title'}).string)
    # CSS选择器
    # for item in soup.select('.hd'):
    #     movie_top_250.append(item.select_one('.title').string)

    # pyquery
    # doc = pq(html)
    # items = doc('.hd').children().items()
    # for item in items:
    #     movie_top_250.append(item.text())


def main():
    url = 'https://www.beqege.com/61536/82048'
    # data1 = "?start="
    # data2 = "&filter="
    for i in range(817):
        html = get_one_page(url+str(i+1)+'.html')  // 将要爬取的网页写成这种形式进行爬取
        parse_one_page(html)
        print(i+1)

    # html = get_one_page(url)
    # print(type(html))
    # print(html)
    # with open('tt.txt', mode='w+', encoding='utf8') as f:
    #     f.write(html)
    #     print(f)
    #
    # parse_one_page(html.read())
    # print(txt.read())
    txt.close()
    browser.close()


main()
