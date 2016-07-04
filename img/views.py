from django.shortcuts import render

# Create your views here.

def img(req):
    data={}
    return render(req,'img.html',data)

def pub(req):
    data={}
    return render(req,'pub.html',data)