"""
自定义函数库
"""

def error(str='error',uri=''):
    """
    show error message and jump to a new url
    :param str:
    :param uri:
    :return:
    """
    from django.http import HttpResponse
    return HttpResponse(str)

def getext(str):
    """
    get ext of a file
    :param str:
    :return:
    """
    return str.split('.')[-1]

def sm(ob):
    '''
    show message about object
    :param ob:
    :return:
    '''
    print(dir(ob))
    print(type(ob))
    print(ob)

def readcontent(path):
    '''
    read and return file cotent
    :param path:
    :return:
    '''
    op = open(path)
    re =op.read()
    op.close()
    return re

def F(key=None,value=None,path='.'):
    """
    fast key value method
    :param key:
    :param value:
    :param path:
    :return:
    """
    path = path+'/'+key+'.txt'
    if value==None:
        op = open(path,'r')
        re = op.read()
        op.close()
        return re
    else:
        op = open(path, 'w')
        op.write(value)
        op.close()

def bga(req,data={}):
    """
    tmp code as a view in blog
    :param req:
    :param data:
    :return:
    """
    req = req
    from django.template import loader
    return loader.render_to_string('bga.html',data)

def read_image(oldpath,newpath="static/img/"):
    import os
    import uuid
    import time
    data = {}
    data['name'] = oldpath.split('/')[-2]
    data['url'] = []
    if os.path.exists(oldpath):
        re = os.listdir(oldpath)
        newpathadd = newpath+ time.strftime("%y%m%d") + '/' + str(int(time.time() * 100000)) + '/'
        os.makedirs(newpathadd)
        os.rename(oldpath, newpathadd)
        for x in re:
            oldname = newpathadd + x
            newname = newpathadd+ str(uuid.uuid1()) + '.' + getext(x)
            data['url'].append(newname)
            os.rename(oldname, newname)
    return data

def resize_image(inpath,savepath,long=300,mode=1):
    """
    mode = 1 width first
    mode = 2 height first
    mode = 3 width and height
    mode = 4 center crop origin size
    mode = 5 center crop default size
    :param inpath:
    :param savepath:
    :param width:
    :param mode:
    :return:
    """
    import PIL
    img = PIL.Image.open(inpath)
    w = int(img.size[0])
    h = int(img.size[1])

    if mode == 1:
        width = int(long)
        height = int(width/w*h)
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
    if mode == 2:
        height = int(long)
        width = int(height / h * w)
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
    if mode == 3:
        if w>h:
            height = int(long)
            width = int(height / h * w)
        else:
            height = int(long)
            width = int(height / h * w)
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
    if mode == 4 or mode ==5:
        if w >=h:
            l=int((w-h)/2)
            t=int(0)
            r=int((w+h)/2)
            b=int(h)
        else:
            l = int(0)
            t = int((h-w)/2)
            r = int(w)
            b = int((h+w)/2)
        region = (l,t,r,b)
        img = img.crop(region)
        if mode ==5:
            img = img.resize((int(long), int(long)), PIL.Image.ANTIALIAS)
    img.save(savepath)

class Page():

    pagecount=1
    pagesize=1
    pagenum=1
    pagenow=1
    limit = 1
    start = 0
    path = ''

    def __init__(self,pagecount,pagesize=1,pagenow=1,path=''):
        import math
        self.pagecount =pagecount
        self.pagesize = pagesize
        self.pagenum = math.ceil(pagecount/pagesize)
        self.pagenow = self.setpagenow(pagenow)
        self.start = int((self.pagenow-1)*pagesize)
        self.limit = int(self.start+pagesize)
        self.path=path

    def setpagenow(self,p):
        if int(p)<1:
            p=1
        if int(p)>self.pagenum:
            p=self.pagenum
        return int(p)

    def show(self):
        import re
        p = self.path
        pfirst =''
        ppre = ''
        pnext = ''
        plast = ''

        pa = re.findall(r"(.*\/\d*)_*(\d*)\.html", str)[0]

        # # p = str(p).encode('utf-8')
        # # p = 'html'.decode('utf-8')
        # pathext= re.findall(r'_*\d*\.html', p)[0]
        # # r= re.match(r'html', "html")
        # pathextlength = len(pathext)
        # p=p[:-pathextlength]

        if 1:
            pfirst = '1'
            # ppre = p[:-5] +'_'+str(self.pagenow-1) + p[-5:]
            ppre = str(self.pagenow - 1) + '.html'
            pnext = str(self.pagenow + 1) + '.html'
            plast = str(self.pagenum) + '.html'
        # r2 = re.match(r'\/$',p)
        # if r2:
        #     pass
            # pfirst = p
            # ppre = str(self.pagenow - 1) + '.html'
            # pnext = str(self.pagenow + 1) + '.html'
            # plast = str(self.pagenum) + '.html'

        # pfirst = str(self.pagenow)+'.html'

        # pfirst = str(self.pagenow)+'.html'
        # pfirst = p[:-5] + p[-5:]
        # pfirst = p[:-5] + p[-5:]
        # return self.path


        return """
        <ul class='pagination'>
        <li><a href='%s'>first</a></li>
        <li><a href='%s'>pre</a></li>
        <li><a href='%s'>next</a></li>
        <li><a href='%s'>last</a></li>
        </ul>%s
        """%(pfirst,ppre,pnext,plast,pa)














