from django.shortcuts import render
from django.shortcuts import redirect
from django.http import *
from blog.models import *
from blog.forms import *
from ku import *
from django.template import loader,RequestContext
from django.views.decorators.http import *
from blog.sec import *
# Create your views here.


# def about(req):


#####################################################################################

def blog(req):
    dd  = {'re':'hello','gan':'zaina'}
    rrr = bga(req,dd)

    # return HttpResponse(req.build_absolute_uri())
    data={}
    # return HttpResponse(rrr)
    data['bga'] = rrr

    # return HttpResponse( data['bga'] )

    data['artf'] = Artf(req.POST)
    data['art'] = Art.objects.all().order_by("-id")

    # data['coo'] = req.session.get('coo','')
    data['username'] = req.COOKIES.get('username','')
    data['coo'] = req.COOKIES.get('coo','nihao')
    data['bga'] = bga(req)
    data['form'] = Artf()
    ren = render(req,'blog.html',data)
    # req.COOKIES.get('coo','nihao')
    if req.method == 'POST':
        req.session['coo'] = req.POST['coo']

        rep = HttpResponseRedirect("/blog/")
        # rep.cookies['']
        rep.set_cookie('coo', req.POST['coo'])
        return rep
    return ren

def blogadd(req):
    if req.method=="POST":
        if not req.POST['title']:
            title = req.POST['content'][:10]
        else:
            title = req.POST['title']
        content = req.POST['content']
        if content:
            Art.objects.create(title=title,content=content)
    return HttpResponseRedirect("/blog/")

def blogde(req):
    Art.objects.filter(id=req.GET['id']).delete()
    return HttpResponseRedirect("/blog/")

def blogcon(req,id):
    data = {}
    data['art']=Art.objects.get(id=id)
    return render(req, 'blogcon.html', data)

######################################################################################
def userregister(req):
    data={}
    if req.method == 'POST':
        if req.POST['username'] and req.POST['password']:
            if not User.objects.filter(username = req.POST['username']):
                User.objects.create(username = req.POST['username'],password = req.POST['password'],createtime="2010-10-10 12:10:10")
                return HttpResponseRedirect("/userlogin/")
    return render(req,'userregister.html',data)

def userlogin(req):
    data={}
    if req.method == 'POST':
        if req.POST['username'] and req.POST['password']:
            re = User.objects.filter(username=req.POST['username'],password = req.POST['password'])
            if re:
                rep = HttpResponseRedirect("/blog/")
                rep.set_cookie('username',req.POST['username'])
                return rep
            else:
                # return HttpResponse('shibai')
                return error('cuowu')
    return render(req,'userlogin.html',data)

######################################################################################

def savefile(file,path='static/'):
    import time
    newpath = path+time.strftime("%Y%m%d%H%M%S")+'.'+getext(file.name)
    op = open(newpath, 'wb')
    for ck in file.chunks():
        op.write(ck)
    op.close()

def blogfile(req):
    data ={}
    if req.method == 'POST':
        try :
            savefile(req.FILES['file'])
            return HttpResponseRedirect("/blogfile/")
        except:
            pass
        # data['name']=file.size
    return render(req,'blogfile.html',data)