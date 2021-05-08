from django.shortcuts import render
from .models import Task


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
			status = False
			Task.objects.create(title=title, status=status)

	return render(request, 'task_app/create-task.html', context={})
