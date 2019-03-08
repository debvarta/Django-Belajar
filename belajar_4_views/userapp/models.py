# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserModel(models.Model):
    nama = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    alamat = models.TextField()
    email = models.EmailField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.username)
