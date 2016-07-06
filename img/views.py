from django.shortcuts import render
from .models import *
from django.http import *
from ku import *
import os



# -----------------------------form-start--------------------------------------------s
from django import forms

class UpF(forms.Form):
    iname = forms.CharField(max_length=255,widget=forms.Textarea(attrs={'class': 'form-control'}))
    file = forms.FileField(widget=forms.Textarea(attrs={'class': 'form-control'}))


# -----------------------------from-end----------------------------------------------e

# -----------------------------fucntion-start------------------------------------------s
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

def read_period(path,sid=0):
    import time
    re =read_image(path,"static/img/",)
    if re['url']:
        pfaceurlold = re['url'][0]
        if not os.path.exists("static/img/face/"):
            os.makedirs("static/img/face/")
        pfaceurlnew = "static/img/face/"+str(int(time.time() * 100000))+".jpg"
        resize_image(pfaceurlold, pfaceurlnew, 360, 5)
        Period.objects.create(pname=re['name'],sid=sid,pface = pfaceurlnew)
        last =Period.objects.last()
        for x in re['url']:
            Image.objects.create(pid = last.id,iurl = x,sid=sid)

# -----------------------------fucntion-end------------------------------------------e

# -----------------------------view-start--------------------------------------------s
def img(req):
    data={}
    data['period'] = Period.objects.values().order_by("-id")
    data['series'] = Series.objects.values().order_by("-id")
    return render(req,'img.html',data)

def series(req,sid,page=1):
    data={}
    count = Period.objects.filter(sid=sid).count()
    page = Page(count, 2, page, req.get_full_path())
    data['show'] = page.show()
    data['period'] = Period.objects.filter(sid=sid)[page.start:page.limit]
    return render(req,'series.html',data)


def image(req,id,page=1):
    data={}
    count = Image.objects.filter(pid =id).count()
    page = Page(count,1,page,req.get_full_path())
    data['image'] =Image.objects.filter(pid=id)[page.start:page.limit]
    data['show'] = page.show()
    # data['req'] =req
    return render(req,'image.html',data)

def pub(req):
    data={}
    if req.method=="POST":
        if req.FILES:
            data['re'] = 123
            file = req.FILES['file']
            dd = handle_uploaded_file(file)
            data['url'] = dd['path']
            Image.objects.create(iname=req.POST['iname'],iurl=data['url'])
            return HttpResponseRedirect("/")
    return render(req,'pub.html',data)

def show(req):
    resize_image("static/1.jpg","static/3.jpg",300,4)
    return HttpResponse(12)
    return render(req,'show.html',data)


def read_in_sql(req):
    data = {}
    data['series'] = Series.objects.values()
    if req.method=='POST':
        sid = req.POST.get('sid', 0)
        path = 'static/tmp/'
        path_son = os.listdir(path)
        for x in path_son:
            path_whole = path + x + '/'
            read_period(path_whole,sid)
        data['path'] = os.listdir(path)
    return render(req,'du.html',data)

def clear_sql(req):
    Period.objects.filter(id__lte =600).delete()
    Image.objects.filter(id__lte =600).delete()
    return HttpResponse('yes')
# -----------------------------view-end---------------------------------------------e