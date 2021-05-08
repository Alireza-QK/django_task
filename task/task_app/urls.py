from django.urls import path
from .views import homePage, CreateTaskPage, deleteTask, EditTaskPage

app_name = 'task'

urlpatterns = [
	path('', homePage, name='home'),
	path('create-task', CreateTaskPage, name='create-task'),
	path('delete-task/<int:pk>', deleteTask, name='delete-task'),
	path('edit-task/<int:pk>', EditTaskPage, name='edit-task'),
]