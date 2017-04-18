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

def getImg(url):
    html = getHtml(url)
    reg = r'<meta property="og:image" content="(https*://68.media.tumblr.com/.*?\.(jpg|gif|png))" />'
    imgre = re.compile(reg)
    imglist_none = re.findall(imgre, html)
    imglist = list(set(imglist_none))

    if imglist:
        PrePostname = getPostname(url)
        txt = re.search('/', PrePostname)
        if txt:
            Postnames = PrePostname.split('/')
            Postname =Postnames[0]
            # print(PrePostname,Postnames)
        else:
            Postname = PrePostname
        print(len(imglist))
        print(imglist)
        i = 0
        path = 'Tumblrimgdownload/'
        if not os.path.exists(path):
            os.makedirs(path)
        for imgurls in imglist:
            Name = Postname + '_' + str(i)
            imgurl = imgurls[0]
            Postfix = imgurls[1]

            target = path + '%s.%s' % (Name,Postfix)
            i += 1
            print("Downloading %s \n" % target)
            try:
                urllib.request.urlretrieve(imgurl, target)
            except:
                print('The image is lost.')
        return True

