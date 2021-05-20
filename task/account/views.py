from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .forms import UserRegisterForm


def loginView(request):
	return HttpResponse('My loginView')


def RegisterView(request):
	form = UserRegisterForm(request.POST or None)

	context = {
		'form': form
	}
	return render(request, 'account/register.html', context)