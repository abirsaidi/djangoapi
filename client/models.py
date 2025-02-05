from django.db import models

# Create your models here. 

from django.contrib.auth.models import AbstractBaseUser

class CustomClient(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    id=models.AutoField(primary_key=True)

    USERNAME_FIELD = 'email'  # Login with email instead of username
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
