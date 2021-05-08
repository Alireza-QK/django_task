from django.urls import path
from .views import homePage, CreateTaskPage, StatusTaskPage

app_name = 'task'

urlpatterns = [
	path('', homePage, name='home'),
	path('create', CreateTaskPage, name='create-task'),
	path('status', StatusTaskPage, name='status-task'),
]