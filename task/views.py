from django.shortcuts import render
from task.models import *
from task.form import *
from django.http import *
# Create your views here.

def renwu(req):
    data ={}
    f1 = renf1(req.POST,)
    if req.method=='POST':
        if f1.is_valid():
            f1.save()
        return HttpResponseRedirect('/renwu/')

    data['form'] = f1
    data['re'] = ren1.objects.all().order_by("-id")
    return render(req,'renwu.html',data)


def ren4(req):
    data={}
    form = Ren4f(req.POST)
    f1 = F1(req.POST)
    data['form']=form
    data['f1']=f1

    if req.method == 'POST':

        # if not f1.is_valid():
        #     return HttpResponse('f1 not')
        if not form.is_valid():
            return HttpResponse('form2 not')
        else:
            form.save()
            return HttpResponseRedirect("/ren4/")


    req.session['age']=1
    req.session['hi']=2
    req.session['nihao']='nishishui'
    rep=HttpResponse()
    # rep.set_cookie('name','mike')
    # return rep


    # data['ss'] =req.COOKIES['age2']


    data['re'] = Ren4.objects.all().order_by("-id")
    re = render(req,'ren4.html',data)
    re.set_cookie('age2',12)
    return re