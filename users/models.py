from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_student  = models.BooleanField(default = False)
    is_faculty  = models.BooleanField(default = False)

