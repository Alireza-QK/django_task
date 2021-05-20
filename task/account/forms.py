from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].help_text = ''
		self.fields['password1'].help_text = ''
		self.fields['password2'].help_text = ''
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	email = forms.EmailField(
		label='Email',
		required=True,
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
	)

	mobile = forms.RegexField(
		regex=r'(0|\+98)?([ ]|,|-|[()]){0,2}9[1|2|3|4]([ ]|,|-|[()]){0,2}(?:[0-9]([ ]|,|-|[()]){0,2}){8}',
		label='Phone number',
		help_text='Please enter a phone number iranian',
		widget=forms.NumberInput(attrs={'class': 'form-control'}),
		error_messages={
			'invalid': 'this phone number not valid'
		}
	)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'mobile', 'password1', 'password2')

	def clean_mobile(self):
		cleaned_data = super().clean()
		mobile = cleaned_data.get('mobile')
		# Check this phone number already register
		if User.objects.filter(mobile=mobile).exists():
			raise forms.ValidationError('This phone number already register.')
		return mobile