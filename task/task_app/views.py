from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Task
from .forms import TaskForm


def homePage(request):
	context = {
		'tasks': Task.objects.order_by('-created_at').all()
	}
	return render(request, 'task_app/index.html', context=context)


class CreateTaskView(CreateView):
	template_name = 'task_app/create-task.html'
	model = Task
	form_class = TaskForm
	success_url = '/'


class UpdateTaskView(UpdateView):
	template_name = 'task_app/edit-task.html'
	model = Task
	fields = ['title']
	success_url = '/'


class DeleteTaskView(DeleteView):
	model = Task
	template_name = 'task_app/delete-task.html'
	success_url = reverse_lazy('task:home')
