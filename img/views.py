from django.shortcuts import render
from .models import *
from django.http import *

# Create your views here.


# ---------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
def img(req):
    data={}
    data['url'] = image.objects.values().order_by("-id")
    return render(req,'img.html',data)

def pub(req):
    data={}
    if req.method=="POST":
        data['re'] = 123
        file = req.FILES['file']
        # dd = handle_uploaded_file(file)
        # data['url'] = dd['path']
        # image.objects.create(iname='hihi',iurl=data['url'])
        data['rr'] = file
    return render(req,'pub.html',data)