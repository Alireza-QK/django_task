from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', unique=True, max_length=254)
    mobile = models.CharField(verbose_name='Phone number', max_length=11, null=True, blank=True)


    def __str__(self):
        return self.username
