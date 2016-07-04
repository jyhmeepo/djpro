from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.

def read(req):
    data = {}

    if req.method == "POST":
        # wname = req.POST['wname']
        # sname = req.POST['sname']

        # Wen.objects.create(wname = wname,tag=Tags.objects.create(tname='xins'))
        # v = Wen.objects.get(id=3)
        # v = Wen.objects.all()
        # t1 = Tags.objects.get(id=4)
        # v.tag.add(t1)
        # v.save()

        # t1 = Tags.objects.create(sname = 'xins')
        # v = Video(wname=wname)



        return HttpResponseRedirect("/read/")

    data['re'] = Wen.objects.raw("select * from read_wen")
    # data['re'] = Wen.objects.values().filter(wname__regex=r'1')
    # data['re'] = Wen.objects.filter(id__gte = 2)12

    return render(req,'read.html',data)
    # return HttpResponse('read')