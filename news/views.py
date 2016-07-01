from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from news.form import *

def art(req):
    data ={}

    name  = mform(req.POST)

    if req.method=='POST':

        # if name.is_valid():
        #     Mei16.objects.create(name=req.POST['name'],content=req.POST['content'])

        # Mei16.objects.create(name=req.POST['name'], content=req.POST['content'])

        name.save()
        data['name'] = 'yes'
        return HttpResponseRedirect("/art/")

    data['name'] = name
    data['re'] =Mei16.objects.all().order_by("-id")

    return render(req,'art.html',data)