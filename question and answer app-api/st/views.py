from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Log, Student, Question, Answers, Topic
from st.serializers import LoginStudentSerializer, StudentRegisterSerializer, TopicSerializer, AnswersSerializer, QuestionSerializer

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    return render(request, 'register.html')

def logs(request):
    return render(request, 'page-login.html')

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
       
        if (Log.objects.filter(username=email)):
            return Response({'message': 'Duplicate Image Found!'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data = {'username': email, 'password':password})

        if serializer_login.is_valid():
            log = serializer_login.save()
            login_id = log.id
            print(login_id)
        serializer = self.serializer_class(data= {'name':name, 'email':email,'phonenumber':phonenumber, 'place':place, 'post':post, 'pincode':pincode, 'password':password, 'log_id':login_id})

        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Student registered successfully', 'success':1}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':0}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):
    serializer_class = LoginStudentSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        logreg = Log.objects.filter(username=username, password=password)
        if (logreg.exists()):
            read_serializer = LoginStudentSerializer(logreg, many=True)
            for i in read_serializer.data:
                id = i['id']
            return Response({'data':{'id':id, 'username':username},'success': 1, 'message':'Logged in successfully'}, status=status.HTTP_200_OK)       
        else:
            return Response({'data':'username or password is invalid' }, status = status.HTTP_400_BAD_REQUEST)
        

class AddTopicAPIView(GenericAPIView):
     
    serializer_class =  TopicSerializer
    def post(self, request):
        topics = request.data.get('topic')
        serializer = self.serializer_class(data={'topic':topics})
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Topic added successfully', 'success': 1}, status= status.HTTP_201_CREATED)
        
        return Response({'data': serializer.errors, 'message': 'failed to add topic', 'success': 0}, status= status.HTTP_400_BAD_REQUEST)


class TopicsAPIView(GenericAPIView):
    serializer_class =  TopicSerializer
    def get(self, request):
        topics = request.data.get('topic')
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response({'data':serializer.data})

class AddQuestionAPIView(GenericAPIView):
    serializer_class = QuestionSerializer
    def post(self, request):
        question = request.data.get('questions')
        topic = request.data.get('topic')
        student = request.data.get('student')
        
       
        print(student)
        print(topic)
        st = Student.objects.filter(id=student).values()
        print(st)
        for i in st:
            st_name = i['name']
        tp = Topic.objects.filter(id=topic).values()
        for i in tp:
            tp_topic = i['topic']
        
        print(st_name, tp_topic)
 
        serializer = self.serializer_class(data={'questions':question, 'student':student, 'topic':topic})
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Question added successfully', 'success': 1}, status= status.HTTP_201_CREATED)
        
        return Response({'data': serializer.errors, 'message': 'failed to add questions', 'success': 0}, status= status.HTTP_400_BAD_REQUEST)

class AddAnswersAPIView(GenericAPIView):
    serializer_class = AnswersSerializer
    def post(self, request):
        question = request.data.get('question')
        student = request.data.get('student')
        answer = request.data.get('answer')
        topic = request.data.get('topic')
      
 
        serializer = self.serializer_class(data={'question':question, 'student':student, 'answer':answer, 'topic':topic})
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'answers added successfully', 'success': 1}, status= status.HTTP_201_CREATED)
        
        return Response({'data': serializer.errors, 'message': 'failed to add answers', 'success': 0}, status= status.HTTP_400_BAD_REQUEST)



class AnswersAPIView(GenericAPIView):
    serializer_class = AnswersSerializer
    def get(self, request):
        answers = Answers.objects.all()
        serializer = AnswersSerializer(answers, many=True)
        return Response({'data':serializer.data})

