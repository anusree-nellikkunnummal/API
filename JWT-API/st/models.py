from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userprofile(models.Model):
    USER_ROLE = (
        ('AD', 'Admin'),
        ('USR', 'User')
    )

    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE, primary_key=True)
    emprole = models.CharField(max_length=10, choices=USER_ROLE)

