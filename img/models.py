from django.db import models

# Create your models here.

class Image(models.Model):
    iname = models.CharField(max_length=255,default='')
    iurl = models.CharField(max_length=255,default='')
    pid = models.IntegerField(default=0)

class Period(models.Model):
    pname = models.CharField(max_length=255, default='')
    purl = models.CharField(max_length=255, default='')