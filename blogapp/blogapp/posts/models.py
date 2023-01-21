from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify



class categoria(models.Model):
    categoria=models.CharField(max_length=50)
    def __str__(self): 
        return self.categoria

class Post(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=255)
    post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(categoria,on_delete=models.CASCADE)

