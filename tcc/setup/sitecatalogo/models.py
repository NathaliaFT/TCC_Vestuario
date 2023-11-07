from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings

class Catalogo(models.Model):

    OPTIONS_CATEGORY = [
        ("PORTIFOLIO", "Portfolio"),
        ("PROJETOS", "Projects"),
        ("CLT", "CLT"),
        ("COMUNIDADE", "Community"),
    ]

    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    category = models.CharField(max_length=100, choices=OPTIONS_CATEGORY)
    description = models.TextField()
    path = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    published = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    date_photography = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='photos'
    )

    def __str__(self):
        return self.name



class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=200)  


        