from django.urls import path
from chat import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('room/<int:pk>', views.room, name='room'),
    path('createroom/', views.createroom, name='create-room'),
    path('updateroom/<int:pk>', views.updateroom, name='update-room'),
    path('deleteroom/<int:pk>', views.deleteroom, name='delete-room'),
    path('deletemessage/<int:pk>', views.deletemessage, name='delete-message'),
    path('userprofile/<int:pk>', views.userprofile, name='userprofile'),
    path('topics/', views.topicspage, name='topics'),
    path('activity/', views.activitypage, name='activity'),
]