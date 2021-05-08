from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
	title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Task
		fields = ['title']



