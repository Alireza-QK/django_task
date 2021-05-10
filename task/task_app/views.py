from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
	UpdateView,
	CreateView,
	DeleteView,
	ListView,
)
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    queryset = Task.objects.order_by('-created_at')
    paginate_by = 10
    template_name = "task_app/index.html"


class CreateTaskView(CreateView):
	template_name = 'task_app/create-task.html'
	model = Task
	form_class = TaskForm
	success_url = '/'


class UpdateTaskView(UpdateView):
	template_name = 'task_app/edit-task.html'
	model = Task
	form_class = TaskForm
	success_url = '/'


class DeleteTaskView(DeleteView):
	model = Task
	template_name = 'task_app/delete-task.html'
	success_url = reverse_lazy('task:home')
