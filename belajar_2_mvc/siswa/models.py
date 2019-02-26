# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Siswa(models.Model):
        nisn = models.CharField(max_length=200)
        nama = models.CharField(max_length=200)

        def __str__(self):
                return "{}.{}".format(self.id, self.nisn)

