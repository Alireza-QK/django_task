from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'updated_at')
	ordering = ('-created_at', )

admin.site.register(Task, TaskAdmin)
