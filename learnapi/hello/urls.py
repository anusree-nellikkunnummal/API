from django.urls import path
from hello import views

urlpatterns = [
    path('members', views.members, name='members'),
    path('members/<int:id>', views.members_details, name = 'membersdetails'),
]