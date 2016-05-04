# -*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
from urlparse import urljoin
import threading
from sys import argv

script, baseurl, filetype = argv

def geturls(f):
    urls = []
    soup = BeautifulSoup(f, 'html.parser')
    soup.prettify()

    for anchor in soup.find_all('a', href=True):
        url = anchor['href']
        url = urljoin(baseurl, url)
        if url.find('.' + filetype) > -1:
            urls = urls + [url]
    return urls


def getfile(url):
    fl = url.split('/')[-1]
    print 'downling file ' + fl
    res = urllib2.urlopen(url)
    f = open(fl, 'wb')
    f.write(res.read())
    f.close()
    print fl


if __name__ == '__main__':
    res = urllib2.urlopen(baseurl)
    f = res.read()
    urls = geturls(f)

    threads = []
    for url in urls:
        t = threading.Thread(target = getfile, args = (url,))
        threads.append(t)
    for t in threads:
        t.start()

    for t in threads:
        t.join()
