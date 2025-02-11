from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer
from .models import Category
# Create your views here.
class CategoryCreateview(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
class CategoryDetailView(APIView):
    def get(self,request,pk):
        category=Category.objects.get(idCategory=pk)
        serializer=CategorySerializer(category)
        return Response(serializer.data)
class CategoryUpdateview(APIView):
    def put (self,request,pk):
        category=Category.objects.get(idCategory=pk)
        serializer=CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        category=Category.objects.get(idCategory=pk)
        serializer=CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CategoryDeleteView(APIView):
    def delete(self,request,pk):
        category=Category.objects.get(idCategory=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   