from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.

def read(req):
    data = {}

    if req.method == "POST":
        sname = req.POST['sname']
        Series.objects.create(sname = sname)
        return HttpResponseRedirect("/read/")
    data['re'] = Series.objects.all()

    return render(req,'read.html',data)
    # return HttpResponse('read')