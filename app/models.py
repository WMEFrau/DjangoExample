from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    createdate = models.DateTimeField(auto_now_add=True)
    urlimg=models.ImageField(upload_to="img/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)