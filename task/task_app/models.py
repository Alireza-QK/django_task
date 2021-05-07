from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
	title = models.CharField(max_length=254, verbose_name='Title')
	status = models.BooleanField(default=False, verbose_name='Status task')
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'task_tbl'
		verbose_name = 'task'
		verbose_name_plural = 'tasks'
		