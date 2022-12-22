from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Log, Student, Teachers, Teacherslog
from st.serializers import LoginStudentSerializer, StudentRegisterSerializer, LoginTeacherSerializer, TeacherRegisterSerializer

# Create your views here.
# def dashboard(request):
#     return render(request, 'dashboard.html')

# def register(request):
#     return render(request, 'register.html')

# def logs(request):
#     return render(request, 'page-login.html')

# class StudentRegisterAPIView(GenericAPIView):
#     serializer_class = StudentRegisterSerializer
#     serializer_class_login = LoginStudentSerializer
#     def post(self, request):
#         name = request.data.get('name')
#         email = request.data.get('email')
#         phonenumber = request.data.get('phonenumber')
#         place = request.data.get('place')
#         post = request.data.get('post')
#         pincode = request.data.get('pincode')
#         password = request.data.get('password')
#         role = request.data.get('role')
#         if (Log.objects.filter(username=email)):
#             return Response({'message': 'Duplicate Image Found!'}, status = status.HTTP_400_BAD_REQUEST)
#         else:
#             serializer_login = self.serializer_class_login(data = {'username': email, 'password':password, 'role':role})

#         if serializer_login.is_valid():
#             log = serializer_login.save()
#             login_id = log.id
#             print(login_id)
#         serializer = self.serializer_class(data= {'name':name, 'email':email,'phonenumber':phonenumber, 'place':place, 'post':post, 'pincode':pincode, 'password':password, 'log_id':login_id, 'role':role})

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data, 'message':'Student registered successfully', 'success':1}, status = status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors, 'message':'Failed','success':0}, status=status.HTTP_400_BAD_REQUEST)

# class LoginAPIView(GenericAPIView):
#     serializer_class = LoginStudentSerializer
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         role = request.data.get('role')
#         logreg = Log.objects.filter(username=username, password=password)
#         if (logreg.count()>0):
#             read_serializer = LoginStudentSerializer(logreg, many=True)
#             for i in read_serializer.data:
#                 id = i['id']
#                 role = i['role']
#             return Response({'data':{'id':id, 'role':role},'success': 1, 'message':'Logged in successfully'}, status=status.HTTP_200_OK)       
#         else:
#             return Response({'data':'username or password is invalid' }, status = status.HTTP_400_BAD_REQUEST)
        

class TeacherRegisterAPIView(GenericAPIView):
    serializer_class = TeacherRegisterSerializer
    serializer_class_login = LoginTeacherSerializer
    def post(self, request):
        name = request.data.get('name')
        username = request.data.get('username')
        email = request.data.get('email')
        phonenumber = request.data.get('phonenumber')
        address = request.data.get('address')
        subject = request.data.get('subject')
        password = request.data.get('password')
        role = request.data.get('role')
        if Teacherslog.objects.filter(username=username):
            return Response({'message': 'Duplicate Image Found!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer_log = self.serializer_class_login(data={'username':username, 'passowrd':password, 'role':role})
            print(serializer_log)
        if serializer_log.is_valid():
            log = serializer_log.save()
            logs_id = log.id
            print(logs_id)
        

        serializer = self.serializer_class(data={'name':name, 'username':username, 'email':email, 'phonenumber':phonenumber, 'address':address, 'subject':subject, 'password':password, 'log_id':logs_id, 'role':role })
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Teacher registered successfully', 'success': 1}, status= status.HTTP_201_CREATED)
        
        return Response({'data': serializer.errors, 'message': 'Teacher registration failed', 'success': 0}, status= status.HTTP_400_BAD_REQUEST)


# class get_studentAPIView(GenericAPIView):
#     serializer_class = StudentRegisterSerializer
#     def get(self, request):
#         queryset = Student.objects.all()
#         if (queryset.count()>0):
#             serializer = StudentRegisterSerializer(queryset, many=True)
#             # for i in serializer.data: 
#                 # login_id = i['log_id']
#                 # name = i['name']
#             return Response({'data': serializer.data, 'message':'data get', 'success':1})
#         else:
#             return Response({'data':'No data available'}, status=status.HTTP_400_BAD_REQUEST)

# class update_studentAPIView(GenericAPIView):
#     serializer_class = StudentRegisterSerializer
#     def put(self, request, id):
#         queryset = Student.objects.get(pk=id)
#         print(queryset)
#         serializer = StudentRegisterSerializer(instance=queryset, data=request.data, partial=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data, 'message':'updated successfully', 'success':1}, status=status.HTTP_200_OK)
            


# class delete_studentAPIView(GenericAPIView):
#     def delete(self, request, id):
#         delmember = Student.objects.get(pk=id)
#         delmember.delete()
#         return Response({'message':'Deleted successfully'})

# class SingleStudentAPIView(GenericAPIView):
#     def get(self, request, id):
#         queryset = Student.objects.get(pk=id)
#         serializer =StudentRegisterSerializer(queryset)
#         return Response(serializer.data)
