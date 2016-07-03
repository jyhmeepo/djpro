from django.db import models

# Create your models here.

class Series(models.Model):
    sname = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.sname

class Pinfo(models.Model):
    infoname = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.infoname

class Image(models.Model):
    iname = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.iname

class Tags(models.Model):
    tname = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.tname

class Period(models.Model):
    sname = models.ForeignKey(Series,default='')
    tag = models.ManyToManyField(Tags,default='')
    infoname = models.OneToOneField(Pinfo,default='')
    pname = models.CharField(max_length=255,default='')
    password = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.pname

class Video(models.Model):
    sname = models.ForeignKey(Series, default='')
    vname = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.vname

class Wen(models.Model):
    tag = models.ManyToManyField(Tags)
    wname = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.wname