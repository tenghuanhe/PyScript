# -*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
from urlparse import urljoin

baseurl = 'http://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/assignments'


def geturls(f):
    urls = []
    soup = BeautifulSoup(f, 'html.parser')
    soup.prettify()

    for anchor in soup.find_all('a', href=True):
        url = anchor['href']
        url = urljoin(baseurl, url)
        if url.find('.pdf') > -1:
            urls = urls + [url]
    return urls


def getpdf(url):
    fl = url.split('/')[-1]
    res = urllib2.urlopen(url)
    f = open(fl, 'wb')
    f.write(res.read())
    f.close()
    print fl


if __name__ == '__main__':
    res = urllib2.urlopen(baseurl)
    f = res.read()
    urls = geturls(f)

    for url in urls:
        getpdf(url)
