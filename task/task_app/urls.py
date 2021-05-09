from django.urls import path
from .views import (homePage, CreateTaskView, DeleteTaskView, UpdateTaskView)

app_name = 'task'

urlpatterns = [
	path('', homePage, name='home'),
	path('create-task', CreateTaskView.as_view(), name='create-task'),
	path('delete-task/<int:pk>', DeleteTaskView.as_view(), name='delete-task'),
	path('edit-task/<int:pk>', UpdateTaskView.as_view(), name='edit-task'),
]