from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.views.generic.edit import UpdateView
from .models import Task
from .forms import TaskForm


def homePage(request):
	context = {
		'tasks': Task.objects.order_by('-created_at').all()
	}
	return render(request, 'task_app/index.html', context=context)


def CreateTaskPage(request):

	form = ''
	if request.method == 'POST':
		form = request.POST

		if form['title_task']:
			title = form['title_task']
			Task.objects.create(title=title)
			return redirect(reverse('task:home'))
		else:
			messages.error(request, "title can't empty", 'danger')

	return render(request, 'task_app/create-task.html', context={})


def deleteTask(request, pk):
	
	if pk:
		try:

			Task.objects.get(pk=pk).delete()
			return redirect(reverse('task:home'))
		except Task.DoesNotExist:
			redirect(reverse('task:home'))	

	return redirect(reverse('task:home'))


def EditTaskPage(request, pk):

	context ={}
	obj = get_object_or_404(Task, pk = pk)
	form = TaskForm(request.POST or None, instance=obj or None)

	if form.is_valid():
		# save the form data to model
		form.save()
		return redirect(reverse('task:home'))
	
	context['form'] = form
	return render(request, 'task_app/edit-task.html', context)

