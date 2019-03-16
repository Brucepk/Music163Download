import lyrics163
import urllib
import time

'''
作者：pk哥
公众号：Python知识圈
日期：2018/08/10
代码解析详见公众号「Python知识圈」。

'''


def save_song(songurl, path):
    try:
        urllib.request.urlretrieve(songurl, path)
        print('歌曲下载完成：' + songname)
    except BaseException:
        print('下载失败：' + songname)
        pass


if __name__ == '__main__':
    # 张韶涵 id = '10562'
    id = input('请输入歌手id：')
    top50url = 'https://music.163.com/artist?id={}'.format(id)
    html = lyrics163.get_html(top50url)
    singer_infos = lyrics163.get_top50(html)
    for singer_info in singer_infos:
        songid = singer_info[1]
        songurl = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(songid)
        songname = singer_info[0]
        path = 'E:\\song\\' + songname + '.mp3'
        save_song(songurl, path)
        time.sleep(1)


