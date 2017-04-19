import re
import traceback
from urllib import quote
import urllib
import TumblrVideo
import TumblrImage


def getHtml(url):
    url = quote(url, safe='/:?=')
    page = urllib.urlopen(url)
    html = page.read().decode('utf-8')
    return html


def vedio_image_judge(url):
    html = getHtml(url)
    reg = r'<meta property="og:type" content="tumblr-feed:(.*?)" />'
    typere = re.compile(reg)
    type =re.findall(typere, html)
    if type:
        print('This is %s' % type[0])
        return type[0]
    else:
        return False

def PostDownload(url):
    Type =vedio_image_judge(url)

    if Type == 'video':
        TumblrVideo.getMP4(url)
    elif Type == 'photoset' or 'photo':
        TumblrImage.getImg(url)
    else:
        print('There is nothing!')



