from hello.models import Member
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        def create(self, validated_data):
            return Member.objects.create(**validated_data)
     