from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse


def profile(request):
    return HttpResponse('My profile')
