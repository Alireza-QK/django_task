from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'ststus', 'created_at', 'updated_at')
	ordering = ('-created_at', 'status')

admin.site.register(Task, TaskAdmin)
