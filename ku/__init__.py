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

def handle_uploaded_file(f):
    """
    save upload file
    :param f:
    :return:
    """
    import os
    import time
    file_path = 'static/img/'+str(int(time.time()))+'.'+getext(f.name)
    data = {}
    data['path'] = file_path
    data['name'] = 'name'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return data

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
        data['path'] = newpathadd
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
        if re.search("/$", p):
            p = p[:-1]
        pa = re.findall(r"(.*\/)(\d*)(_*\d*)(\.html$)*", p)[0]
        def crurl(page,tu,pagenum):
            if int(page) <1:
                return ''
            if int(page) > pagenum:
                return ''
            return "href='"+tu[0]+tu[1]+'_'+str(page)+tu[3]+"'"

        pfirst = '1'
        ppre = (self.pagenow - 1)
        pnext = (self.pagenow + 1)
        plast = (self.pagenum)

        pfirst = crurl(pfirst,pa,self.pagenum)
        ppre = crurl(ppre,pa,self.pagenum)
        pnext = crurl(pnext,pa,self.pagenum)
        plast = crurl(plast,pa,self.pagenum)

        return """
        <ul class='pagination'>
        <li><a %s >first</a></li>
        <li><a %s >pre page</a></li>
        <li><a %s >next page</a></li>
        <li><a %s >last</a></li>
        </ul>
        """%(pfirst,ppre,pnext,plast)














