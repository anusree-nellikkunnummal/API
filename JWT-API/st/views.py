from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from st.serializers import MyTokenObtainPairSerializer
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

