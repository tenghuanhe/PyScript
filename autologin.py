# coding: utf-8

import urllib2, urllib, re, cookielib, sys
import Image
import chardet

from pytesser.pytesser import image_file_to_string
from ImageColor import str2int

cookiejar = cookielib.CookieJar()
urlopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
urllib2.install_opener(urlopener)

url = 'http://bitunion.org/'
html = urllib2.urlopen(url).read()

re_png = re.compile(r'verifyimg.php\?id=\w+')
png_url = url + re.findall(re_png, html)[0]

verifyid = png_url.split('=')[-1]
print verifyid

local_png = '1.png'

urllib.urlretrieve(png_url, local_png)

file_data = Image.open(local_png)

file_data = file_data.convert('RGB')

width, height = file_data.size

data = file_data.load()

for i in range(width):
    for j in range(height):
        if not data[i, j] == (0, 0, 0):
            data[i, j] = (255, 255, 255)

file_data.save('2.png')

verify_code = str(str2int(image_file_to_string('2.png')))

print verify_code

data_post = urllib.urlencode({
    'referer'       :'/home.php?',
    'username'      :'he21th',
    'password'      :'welcome2bitunion',
    'verify'        :verify_code,
    'verifyimgid'   :verifyid,
    'styleid'       :'',
    'cookietime'    :'0',
    'loginsubmit'   :'登录'
})

req = urllib2.Request(
    url = 'http://bitunion.org/logging.php?action=login&referer=%2F',
    data = data_post
)

content = urllib2.urlopen(req).read()

sys_encode = sys.getfilesystemencoding()

info_encode = chardet.detect(content).get('encoding', 'utf-8')

html = content.decode(info_encode, 'ignore').encode(sys_encode)

html = urllib2.urlopen(url).read()

print html

