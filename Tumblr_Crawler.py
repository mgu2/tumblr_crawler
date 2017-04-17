import re
import time

def Main_Post_URLDiscrimination(url):
    post_reg = r'(.*?/post/.*?/*.*)'
    # post_re = re.compile(post_reg)
    # post_discrimination = re.findall(post_re, url)
    post_discrimination = re.match(post_reg, url)
    if post_discrimination:
        print('A Post page!')
        return False
    else:
        print('This is Main page!')
        return True


if __name__ == '__main__':
    select = 'Y'
    reg = r'(http||https)://.*?'
    while select == 'Y':
        URL = input('Input url: ')
        if re.match(reg, URL):
            discrimination = Main_Post_URLDiscrimination(URL)
            start = time.time()
            if discrimination:
                DownloadAllthepsot(URL)
            else:
                TumblrPostDownload.PostDownload(URL)
            end =time.time()
            print(start, end, '=> Cost %ss' % (end - start))
        else:
            print('wrong input')

        select = input('do you want to continue?[Y/N]')