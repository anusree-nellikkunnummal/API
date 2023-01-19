from django.db import models

# Create your models here.
class Log(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, unique=True)
   
    def __str__(self):
        return self.username

class Student(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 20)
    phonenumber = models.CharField(max_length = 20)
    place = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    pincode = models.CharField(max_length = 20)
    password = models.CharField(max_length=20)
    log_id = models.OneToOneField(Log, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

class Question (models.Model):
    student = models.ForeignKey(Log, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    questions = models.CharField(max_length=20) 
   
    def __str__(self):
        return self.questions[:15]

class Answers(models.Model):

    student = models.ForeignKey(Log, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    answer = models.CharField(max_length=600)
  
    def __str__(self):
        return self.answer[:15]

