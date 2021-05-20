from django.urls import path,re_path
from .views import (
	loginView,
	RegisterView,
)

app_name = 'account'

urlpatterns = [
	path('login', loginView, name="login"),
	path('register', RegisterView, name="register"),
]
