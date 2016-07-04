from django.shortcuts import render
from .models import *
from django.http import *
from ku import *



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

# -----------------------------fucntion-end------------------------------------------e

# -----------------------------view-start--------------------------------------------s
def img(req):
    data={}
    data['period'] = Period.objects.values().order_by("-id")
    return render(req,'img.html',data)

def image(req,id):
    data={}
    data['image'] = Image.objects.filter(pid =id)
    data['id'] = id
    return render(req,'image.html',data)

def pub(req):
    data={}
    # data['form'] = UpF()
    if req.method=="POST":
        if req.FILES:
            data['re'] = 123
            file = req.FILES['file']
            dd = handle_uploaded_file(file)
            data['url'] = dd['path']

            Image.objects.create(iname=req.POST['iname'],iurl=data['url'])
            # data['rr'] = file
            return HttpResponseRedirect("/")
    return render(req,'pub.html',data)

def show(req):
    data ={}
    re =read_image("static/tmp/","static/img/",)
    Period.objects.create(pname=re['title'])
    last =Period.objects.last()
    for x in re['path']:
        Image.objects.create(pid = last.id,iurl = x)
    data['re'] =last
    return render(req,'show.html',data)
# -----------------------------view-end---------------------------------------------e