from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Userprofile

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attr):
        data = super().validate(attr)
        token = self.get_token(self.user)
        data['user'] = str(self.user)
        data['id'] = self.user.id
        userProfileobj = Userprofile.objects.get(user=self.user)
        data['emprole'] = userProfileobj.emprole
        return data




   