import re
import urllib.request
from urllib import quote

def getHtml(url):
    url = quote(url, safe='/:?=')
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        return html
    except:
        # traceback.print_exc()
        print('The URL you requested could not be found')
        return 'Html'

def BlogStyleDetection(url):
    html = getHtml(url)
    reg = 'https://secure.static.tumblr.com/szeoxcc/Ms9on6cqn/main-min.css'
    defaultStylere = re.compile(reg)
    detection = re.findall(defaultStylere, html)

    if detection:
        print('Default theme')
        return True
    else:
        print('Using personal theme!')
        return False