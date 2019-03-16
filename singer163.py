from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import csv

'''
作者：pk哥
公众号：Python知识圈
日期：2018/08/10
代码解析详见公众号「Python知识圈」。

'''

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 5)  # 设置等待时间


def get_singer(url):    # 返回歌手名字和歌手id
    browser.get(url)
    browser.switch_to.frame('g_iframe')
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    info = soup.select('.nm.nm-icn.f-thide.s-fc0')
    singername = []
    singerid = []
    for snames in info:
        name = snames.get_text()
        songid = str(re.findall('href="(.*?)"', str(snames))).split('=')[1].split('\'')[0]
        singername.append(name)
        singerid.append(songid)
    return zip(singername, singerid)


def get_data(url):
    data = []
    for singernames, singerids in get_singer(url):
        info = {}
        info['歌手名字'] = singernames
        info['歌手ID'] = singerids
        data.append(info)
    return data


def save2csv(url):
    print('保存歌手信息中...请稍后查看')
    with open('E:\\热门歌手信息.csv', 'a', newline='', encoding='utf-8-sig') as f:
        # CSV 基本写入用 w，追加改模式 w 为 a
        fieldnames = ['歌手名字', '歌手ID']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        data = get_data(url)
        print(data)
        writer.writerows(data)
        print('保存成功')


if __name__ == '__main__':
    idlist = [1001, 1002, 1003, 2001, 2002, 2003, 4001, 4002, 4003, 6001, 6002, 6003, 7001, 7002, 7003]
    for id in idlist:
        url = 'https://music.163.com/#/discover/artist/cat?id={}&initial=-1'.format(id)
        save2csv(url)