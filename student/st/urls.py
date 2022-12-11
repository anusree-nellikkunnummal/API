from django.urls import path
from . import views

urlpatterns = [
    
    path('student_register', views.StudentRegisterAPIView.as_view(), name='student_register'),

]