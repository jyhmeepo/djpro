from ku import *
import math
import random
import os
import time
from PIL import Image
import re
from django.core.urlresolvers import reverse
import datetime
import urllib3


def crurl(page, tu, pagenum):
    if int(page) < 1:
        return ''
    if int(page) > pagenum:
        return ''
    return "href='" + tu[0] + tu[1] + '_' + str(page) + tu[3] + "'"

def makepage(url):
    import urllib.parse
    import re
    urlin = urllib.parse.urlparse(url)

    # data = {}
    # data['scheme'] = urlin.scheme
    # data['netloc'] = urlin.netloc
    # data['path'] = urlin.path
    # data['params'] = urlin.params
    # data['query'] = urlin.query
    # data['fragment'] = urlin.fragment
    path = urlin.path
    if re.search("/$", path):
        path = path[:-1]
    match = re.findall(r"(.*\/)(\d*)(_*\d*)(\.html)*", path)
    # html = crurl(2,match,10)
    if urlin.query:
        urlout = path + '?'+urlin.query
        
    return match

# url = "http://www.baidu.com/search/1_1.html?s=1&b=2#jj"
# url = "http://www.baidu.com/search/1_1/?s=1&b=2#jj"
url = "http://www.baidu.com/search/?s=1&b=2#jj"
re = makepage(url)
print(
    (re)
)