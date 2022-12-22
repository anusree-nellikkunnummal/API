from django.urls import path
from . import views

urlpatterns = [
    
#     path('student_register', views.StudentRegisterAPIView.as_view(), name='student_register'),
#     path('login_show', views.LoginAPIView.as_view(), name='login_show'),
      path('teacher_register', views.TeacherRegisterAPIView.as_view(), name='teacher_register'),
#     path('get_student', views.get_studentAPIView.as_view(), name='get_student'),
#     path('delete_student/<int:id>', views.delete_studentAPIView.as_view(), name='delete_student'),
#     path('update_student/<int:id>', views.update_studentAPIView.as_view(), name='update_student'),
#     path('single_student/<int:id>', views.SingleStudentAPIView.as_view(), name='single_student'),

]