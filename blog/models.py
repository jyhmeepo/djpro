from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255,default='')
    password = models.CharField(max_length=255,default='')
    createtime =models.DateTimeField()
    def __str__(self):
        return self.username

class Art(models.Model):
    title = models.CharField(max_length=255,default='')
    content = models.TextField(default='')
    def __str__(self):
        return self.title