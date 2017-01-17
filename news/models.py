from __future__ import unicode_literals

# Create your models here.

from django.db import models


class News(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    URL = models.CharField(max_length=100)
    score = models.IntegerField()
    sentiment = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)