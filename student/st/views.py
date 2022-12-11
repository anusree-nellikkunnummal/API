from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Log, Student
from st.serializers import LoginStudentSerializer, StudentRegisterSerializer

# Create your views here.
# def dashboard(request):
#     return render(request, 'dashboard.html')

# def register(request):
#     return render(request, 'register.html')

# def logs(request):
#     return render(request, 'page-login.html')

class StudentRegisterAPIView(GenericAPIView):
    serializer_class = StudentRegisterSerializer
    serializer_class_login = LoginStudentSerializer
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        phonenumber = request.data.get('phonenumber')
        place = request.data.get('place')
        post = request.data.get('post')
        pincode = request.data.get('pincode')
        password = request.data.get('password')
        role = request.data.get('role')
        if (Log.objects.filter(username=email)):
            return Response({'message': 'Duplicate Image Found!'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data = {'username': email, 'password':password, 'role':role})

        if serializer_login.is_valid():
            log = serializer_login.save()
            login_id = log.id
            print(login_id)
        serializer = self.serializer_class(data= {'name':name, 'email':email,'phonenumber':phonenumber, 'place':place, 'post':post, 'pincode':pincode, 'password':password, 'log_id':login_id, 'role':role})

        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Student registered successfully', 'success':1}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':0}, status=status.HTTP_400_BAD_REQUEST)