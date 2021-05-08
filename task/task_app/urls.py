from django.urls import path
from .views import homePage

app_name = 'task'

urlpatterns = [
	path('', homePage, name='home')
]