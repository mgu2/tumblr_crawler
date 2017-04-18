import re
from urllib import quote
import urllib
import os


def getHtml(url):
    url = quote(url, safe='/:?=')
    page = urllib.urlopen(url)
    html = page.read().decode('utf-8')
    return html

def getPostname(posturl):
    reg = r'https*://.*?\/post\/(.*)'
    postname = re.compile(reg)
    postnamelist = re.findall(postname, posturl)
    print(postnamelist)
    if postnamelist:
    	return postnamelist[0]
    else:
        postnamelist = ['page1']
        return postnamelist[0]


def getMP4(url):
    html = getHtml(url)
    reg = r'<iframe src=\'(https\://www\.tumblr\.com/video/.*?)\''
    videopagere = re.compile(reg)
    videopageurl = re.findall(videopagere, html)
    if videopageurl:
        print(videopageurl[0])

        videohtml = getHtml(videopageurl[0])
        reg_url = r'<source src="(https://.*?.tumblr.com/video_file/t:.*?)" type="video/mp4">'
        videore = re.compile(reg_url)
        videourl = re.findall(videore, videohtml)[0]
        print(videourl)

        PrePostname = getPostname(url)
        txt = re.search('/', PrePostname)
        if txt:
            Postnames = PrePostname.split('/')
            Name = Postnames[0]

        else:
            Name = PrePostname
        path = 'TumblrMP4download/'
        if not os.path.exists(path):
            os.makedirs(path)
        target = path + '%s.mp4' % Name

        print("Downloading %s " % target)
        try:
            urllib.request.urlretrieve(videourl, target)
        except:
            # traceback.print_exc()
            print('The video is deleted or not found.')
        return True

    else:
        print('There is no Video!')
        return False

