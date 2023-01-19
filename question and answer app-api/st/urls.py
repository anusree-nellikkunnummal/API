from django.urls import path
from . import views

urlpatterns = [
    
    path('student_register', views.StudentRegisterAPIView.as_view(), name='student_register'),
    path('login_show', views.LoginAPIView.as_view(), name='login_show'),
    path('add_topic', views.AddTopicAPIView.as_view(), name='add_topic'),
    path('topics', views.TopicsAPIView.as_view(), name='topics'),
    path('add_question', views.AddQuestionAPIView.as_view(), name='add_question'),
    path('add_answer', views.AddAnswersAPIView.as_view(), name='add_answer'),
    path('answer', views.AnswersAPIView.as_view(), name='answer'),
    # path('get_student', views.get_studentAPIView.as_view(), name='get_student'),
    # path('delete_student/<int:id>', views.delete_studentAPIView.as_view(), name='delete_student'),
    # path('update_student/<int:id>', views.update_studentAPIView.as_view(), name='update_student'),
    # path('single_student/<int:id>', views.SingleStudentAPIView.as_view(), name='single_student'),

]