# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Siswa
# Create your views here.
def LihatSiswa(request):
	Semua_Siswa = Siswa.objects.all()

	context = {
			"Semua_Siswa" : Semua_Siswa,
		}
	return render (request, "siswa/index.html", context)
