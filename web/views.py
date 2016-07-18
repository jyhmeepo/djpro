from django.shortcuts import render
from django.http import *
from .models import *
from ku import *
import os
# Create your views here.


# -----------------------------fucntion-start------------------------------------------s
def read_period(path,fid=0):
    """
    read data in database
    :param path:
    :param sid:
    :return:
    """
    import time
    import os
    re =read_image(path,"static/img/",)
    facesavepath = re['path']
    if re['url']:
        pfaceurlold = re['url'][0]
        if not os.path.exists(facesavepath):
            os.makedirs(facesavepath)
        pfaceurlnew = facesavepath+str(int(time.time() * 10000))+"."+getext(re['url'][0])
        resize_image(pfaceurlold, pfaceurlnew, 360, 5)
        Art.objects.create(aname=re['name'],fid=fid,faceurl = pfaceurlnew)
        last =Art.objects.last()
        for x in re['url']:
            Image.objects.create(aid = last.id,iurl = x,fid=fid)

# -----------------------------fucntion-end------------------------------------------e

# -----------------------------block-start------------------------------------------e
def block_image(fid={},req=None):
    from django.template import loader
    d = {}
    d['forum'] = Forum.objects.get(id=fid)
    d['art'] = Art.objects.filter(fid=fid).values()[:4]
    return loader.render_to_string('block_image.html',d,request=req)
# -----------------------------block-end--------------------------------------------e

# -----------------------------view-start--------------------------------------------s
def main(req):
    data ={}
    data['forum'] = Forum.objects.all()
    # data['bi'] = block_image(1)
    data['url'] = Url.objects.all()
    return render(req,'main.html',data)

def forum(req,fid,page=1):
    data = {}
    count = Art.objects.filter(fid=fid).count()
    if count:
        page = Page(count, 1, page, req.get_full_path())
        data['show'] = page.show()
        data['art'] = Art.objects.filter(fid=fid)[page.start:page.limit]
    data['forum'] = Forum.objects.get(id=fid)
    return render(req,'forum.html',data)

def search(req,page=1):
    data = {}
    count = Art.objects.all().count()
    if count:
        page = Page(count, 1, page, req.get_full_path())
        data['show'] = page.show()
        # data['art'] = Art.objects.filter(fid=fid)[page.start:page.limit]
    # data['forum'] = Forum.objects.get(id=fid)
        data['art'] = Art.objects.all()[page.start:page.limit]
        data['search'] = req.GET.get('search','')
    return render(req,'forum.html',data)

def art(req,aid,page=1):
    data = {}
    count = Image.objects.filter(aid=aid).count()
    page = Page(count, 3, page, req.get_full_path())
    data['image'] = Image.objects.filter(aid=aid)[page.start:page.limit]
    data['show'] = page.show()
    data['art'] = Art.objects.get(id=aid)
    return render(req,'art.html',data)

def read_image_in_sql(req):
    data = {}
    data['forum'] = Forum.objects.values()
    if req.method == 'POST':
        fid = req.POST.get('fid', 0)
        path = 'static/tmp/'
        path_son = os.listdir(path)
        for x in path_son:
            path_whole = path + x + '/'
            read_period(path_whole, fid)
        data['path'] = os.listdir(path)
    return render(req, 'web_read.html', data)

def web_delete(req):
    Art.objects.filter(id__lte=600).delete()
    Image.objects.filter(id__lte=600).delete()
    return HttpResponse('yes')

# -----------------------------view-end---------------------------------------------e
