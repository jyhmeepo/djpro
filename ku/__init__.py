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