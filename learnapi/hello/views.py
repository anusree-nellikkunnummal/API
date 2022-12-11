from django.shortcuts import render
from hello.models import Member
from hello.serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST', 'GET'])
def members(request):
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)
    
    elif request.method == 'GET':
        member = Member.objects.all()
        serializer = MemberSerializer(member, many=True)
        return Response({'data':serializer.data})
    


@api_view(['GET', 'PUT', 'DELETE'])
def members_details(request, id):
    try:
        member = Member.objects.get(pk=id)
    except Member.DoesNotExist:
        return Response({'message':"Item does not exist"},status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response({'data':serializer.data})
    elif request.method == 'PUT':
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data})
        return Response(status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        member.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
   


