from django.shortcuts import render
from django.http.response import HttpResponse


def homePage(request):
	return HttpResponse('Heloo World!')
