from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.

def read(req):
    data = {}

    if req.method == "POST":
        wname = req.POST['wname']
        # sname = req.POST['sname']
        Video.objects.create(wname = wname,tag=Tags(id=1))
        return HttpResponseRedirect("/read/")
    data['re'] = Wen.objects.all()

    return render(req,'read.html',data)
    # return HttpResponse('read')