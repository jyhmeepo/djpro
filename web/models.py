from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255,blank=True,default='')
    password = models.CharField(max_length=255, blank=True, default='')
    faceurl = models.CharField(max_length=255, blank=True, default='')
    status = models.IntegerField(blank=True, default=1)
    createtime = models.IntegerField(blank=True, default=0)
    updatetime = models.IntegerField(blank=True, default=0)
    def __str__(self):
        return self.username

class Forum(models.Model):
    fname = models.CharField(max_length=255,blank=True,default='')
    keywords = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    faceurl = models.CharField(max_length=255,blank=True,default='')
    arttype = models.IntegerField(blank=True,default=1)
    status = models.IntegerField(blank=True,default=1)
    artnumber = models.IntegerField(blank=True, default=0)
    createtime = models.IntegerField(blank=True,default=0)
    updatetime = models.IntegerField(blank=True,default=0)
    def __str__(self):
        return self.fname

class Art(models.Model):
    aname = models.CharField(max_length=255,blank=True,default='')
    faceurl = models.CharField(max_length=255, blank=True, default='')
    content = models.TextField(blank=True, default='')
    keywords = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')

    poster = models.CharField(max_length=255, blank=True, default='')
    videourl = models.CharField(max_length=255, blank=True, default='')
    videotime = models.IntegerField(blank=True,default=0)

    arttype = models.IntegerField(blank=True, default=1)
    status = models.IntegerField(blank=True, default=1)
    fid = models.IntegerField(blank=True,default=0)
    viewnumber = models.IntegerField(blank=True,default=0)
    commentnumber = models.IntegerField(blank=True,default=0)
    imagenumber = models.IntegerField(blank=True,default=0)
    createtime = models.IntegerField(blank=True,default=0)
    updatetime = models.IntegerField(blank=True,default=0)
    def __str__(self):
        return self.aname

class Image(models.Model):
    iname = models.CharField(max_length=255,blank=True,default='')
    iurl = models.CharField(max_length=255,blank=True,default='')
    status = models.IntegerField(blank=True, default=1)
    fid = models.IntegerField(blank=True, default=0)
    aid = models.IntegerField(blank=True, default=0)
    createtime = models.IntegerField(blank=True, default=0)
    updatetime = models.IntegerField(blank=True, default=0)
    def __str__(self):
        return self.iurl

class Url(models.Model):
    webname = models.CharField(max_length=255,blank=True,default='')
    weburl = models.CharField(max_length=255,blank=True,default='')
    status = models.IntegerField(blank=True, default=1)
    sort = models.IntegerField(blank=True, default=1)
    def __str__(self):
        return self.webname