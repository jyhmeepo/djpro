from ku import *
import math
import random
import os
import time
from PIL import Image
import re
from django.core.urlresolvers import reverse
import datetime
# re = os.listdir('1')


# resize_image('1.jpg','2.jpg',360,3)
# r = re.match(r'\d','12')
#
# if r:
#     print(r)

# str ='/s/12_1.html'
str ='/series/1_1/'

if re.search("/$",str):
    str = str[:-1]
print(str)
print(
    re.findall(r"(.*\/)(\d*)(_*\d*)(\.html$)*", str)
)