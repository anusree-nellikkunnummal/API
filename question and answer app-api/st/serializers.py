from rest_framework import serializers
from .models import Log, Student, Topic, Answers, Question

class LoginStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
        
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        def create(self, validated_data):
            return Topic.objects.create(**validated_data)
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__' 
    def create(self, validated_data):
        return Question.objects.create(**validated_data)

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__' 
    def create(self, validated_data):
        return Answers.objects.create(**validated_data)
