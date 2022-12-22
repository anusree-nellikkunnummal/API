from rest_framework import serializers
from .models import Log, Student, Teacherslog, Teachers

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
        
class LoginTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacherslog
        fields = '__all__'
class TeacherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__' 
    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)