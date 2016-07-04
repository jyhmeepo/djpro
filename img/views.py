from django.shortcuts import render
from .models import *
from django.http import *



# -----------------------------form-start--------------------------------------------
from django import forms

class UpF(forms.Form):
    iname = forms.CharField(max_length=255)
    iurl = forms.FileField()


# -----------------------------from-end----------------------------------------------

# -----------------------------fucntion-start------------------------------------------
def handle_uploaded_file(f):
    """
    save upload file
    :param f:
    :return:
    """
    import ku
    import time
    file_path = 'static/img/'+str(int(time.time()))+'.'+ku.getext(f.name)
    data = {}
    data['path'] = file_path
    data['name'] = 'name'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return data

# -----------------------------fucntion-end------------------------------------------

# -----------------------------view-start--------------------------------------------
def img(req):
    data={}
    data['url'] = image.objects.values().order_by("-id")
    return render(req,'img.html',data)

def pub(req):
    data={}
    if req.method=="POST":
        if req.FILES:
            data['re'] = 123
            file = req.FILES['file']
            dd = handle_uploaded_file(file)
            data['url'] = dd['path']
            data['form'] = UpF()
            image.objects.create(iname=req.POST['iname'],iurl=data['url'])
            # data['rr'] = file
    return render(req,'pub.html',data)
# -----------------------------view-end--------------------------------------------