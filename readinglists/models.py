from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(default='', blank=True)
    url = models.CharField(max_length=600)
    tags = TaggableManager()

    def __str__(self):
        return self.name
