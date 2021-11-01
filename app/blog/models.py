from os import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField


STATUS = ((0, "Draft"), (1, "Published"))

class post(models.Model):

    title = models.CharField(max_length=200, )
    slug = models.SlugField(max_length=200, null=True)
    author = models.CharField(max_length=150)
    
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)

class Meta:
    ordering = ['-created_on']


        