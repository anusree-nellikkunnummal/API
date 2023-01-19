from django.contrib import admin
from .models import Log, Student, Topic, Answers, Question

# Register your models here.
admin.site.register(Log)
admin.site.register(Student)
admin.site.register(Topic)
admin.site.register(Answers)
admin.site.register(Question)
