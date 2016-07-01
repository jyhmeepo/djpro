from django.db import models

# Create your models here.

class ren1(models.Model):
    title = models.CharField(max_length=100,default='')
    content = models.CharField(max_length=100,default='')
    choice = {
        ("a","shuxue"),
        ("b","wuli"),
        ("c","yuwen"),
    }
    laoshi = models.CharField(max_length=100,choices=choice,default='a')
    face = models.ImageField(upload_to="static/",default="/")
    def __str__(self):
        return self.title

class ren2(models.Model):
    name = models.CharField(max_length=100,default='')
    age = models.IntegerField(default=0)
    content = models.TextField(default='')

    def __str__(self):
        return self.name

class ren3(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self):
        return self.title

class Ren4(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self):
        return self.title