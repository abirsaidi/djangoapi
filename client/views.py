from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import CustomClient
class ClientCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetailView  (APIView):    
    def get(self,request,pk):
        user=CustomUser.objects.get(id=pk)
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
class ClientListView (APIView):
    def get(self,request):
        users=  CustomUser.objects.all()
        serializer=UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class ClientUpdateView(APIView):
    def put(self,request,pk):
        user=CustomUser.objects.get(id=pk)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data,status=status.HTTP_200_OK)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        user=CustomUser.objects.get(id=pk)
        serializer=UserSerializer(user,data= request.data,partial=True)
        if serializer.is_valid():
            user=serializer.save()
            if user:
                return Response(serializer.data,status=status.HTTP_200_OK)
class UserDeleteView(APIView):
    def delete(self,request,pk):
        user=CustomUser.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                         
