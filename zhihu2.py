#!/usr/bin/python
# -*- coding: utf-8 -*-

import cookielib
import urllib2
import urllib
import gzip
import StringIO
import re
from urlparse import urljoin
from bs4 import BeautifulSoup
import Queue


def getq(fl):
    soup = BeautifulSoup(fl)
    soup.prettify()
    qtitle = soup.find('h2', class_='zm-item-title zm-editable-content')
    if qtitle:
        qtitle = qtitle.contents[0]
        return qtitle.strip()
    else:
        return None


def geturls(fl):
    urls1 = []

    soup = BeautifulSoup(fl)
    soup.prettify()

    baseurl = 'http://www.zhihu.com'
    for anchor in soup.find_all('a', href=True):
        url1 = anchor['href']
        url1 = urljoin(baseurl, url1)
        if url1.find('http://www.zhihu.com/question/') > -1:
            url1 = url1[:38]
            if url1 not in urls:
                urls1 = urls1 + [url1]
    return urls1


if __name__ == '__main__':
    urls = []
    # get hidden _xsrf
    res = urllib2.urlopen('http://www.zhihu.com', timeout=30)
    f = gzip.GzipFile(fileobj=StringIO.StringIO(res.read()), mode='r').read()
    reg = r'name="_xsrf" value="(.*)"/>'
    pattern = re.compile(reg)
    xsrf = pattern.findall(f)[0]

    # login information
    post_params = {'_xsrf': xsrf,
                   'email': 'tenghuanhe@gmail.com',
                   'password': '********',
                   'rememberme': 'y'}

    headers = {'Accept': '*/*',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Accept-Encoding': 'gzip, deflate',
               "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4"}

    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    req = urllib2.Request('http://www.zhihu.com/login', urllib.urlencode(post_params), headers)

    queue = Queue.Queue()
    html = gzip.GzipFile(fileobj=StringIO.StringIO(urllib2.urlopen(req).read()), mode='r').read()

    urlvisited = []
    for url in geturls(html):
        queue.put(url)

    while not queue.empty() and len(urlvisited) <= 1000:
        currenturl = queue.get()
        if currenturl in urlvisited:
            continue
        else:
            try:
                res = urllib2.urlopen(currenturl, timeout=30)
                html = gzip.GzipFile(fileobj=StringIO.StringIO(res.read()), mode='r').read()

                print getq(html)
                for url in geturls(html):
                    queue.put(url)
                urlvisited = urlvisited + [currenturl]
            except urllib2.HTTPError, e:
                pass
