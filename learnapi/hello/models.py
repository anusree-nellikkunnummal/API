from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    def __str__(self):
        return self.name 
        
