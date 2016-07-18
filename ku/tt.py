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
import urllib.parse

url = [
    "http://www.baidu.com/forum/1_1.html?s=1&b=2#jj",
    "http://www.baidu.com/forum/1.html?s=1&b=2#jj",

    "http://www.baidu.com/search/?s=1&b=2#jj",
    "http://www.baidu.com/search_1/?s=1&b=2#jj",

    "http://www.baidu.com/forum/1/",
    "http://www.baidu.com/forum/1_2/",
]

uu = "http://www.baidu.com/search/?s=1&b=2#jj"
u = urllib.parse.urlparse(uu)
# u = urllib.parse.urlunparse(u)
print(u)
sm(u)
exit()
# ---------------------------------------
i = 1
for x in url:
    r =createpageurl(23,11,x)
    print(r)
    i = i + 1
