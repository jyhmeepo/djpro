from django.shortcuts import render
from .models import *
from django.http import *



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

# -----------------------------fucntion-end------------------------------------------e

# -----------------------------view-start--------------------------------------------s
def img(req):
    data={}
    data['url'] = image.objects.values().order_by("-id")
    return render(req,'img.html',data)

def pub(req):
    data={}
    # data['form'] = UpF()
    if req.method=="POST":
        if req.FILES:
            data['re'] = 123
            file = req.FILES['file']
            dd = handle_uploaded_file(file)
            data['url'] = dd['path']

            image.objects.create(iname=req.POST['iname'],iurl=data['url'])
            # data['rr'] = file
            return HttpResponseRedirect("/")
    return render(req,'pub.html',data)
# -----------------------------view-end---------------------------------------------e