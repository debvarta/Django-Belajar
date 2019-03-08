# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserModel

# Create your views here.
def list(request):
	List_User = UserModel.objects.all()

	context = {
		"list_user": List_User
	
	}
	return render(request, 'index.html', context)

