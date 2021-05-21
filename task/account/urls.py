from django.urls import path
from .views import (
    loginView,
    RegisterView,
)

app_name = 'account'

urlpatterns = [
    path('login', loginView, name="login"),
    path('register', RegisterView, name="register"),
]
