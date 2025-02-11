from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarkSerializer
from .models import Mark
# Create your views here.
class MarkCreateView(APIView):
    def post(self, request):
        serializer = MarkSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MarkListView(APIView):
    def get(self, request):
        mark = Mark.objects.all()
        serializer = MarkSerializer(mark, many=True)
        return Response(serializer.data)
class MarkDetailView(APIView):
    def get(self,request,pk):
        mark=Mark.objects.get(idMark=pk)
        serializer=MarkSerializer(mark)
        return Response(serializer.data)
class MarkUpdateView(APIView):
    def put (self,request,pk):
        mark=Mark.objects.get(idMark=pk)
        serializer=MarkSerializer(mark,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        mark=Mark.objects.get(idMark=pk)
        serializer=MarkSerializer(mark,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  class MarkDeleteView(APIView):
    def delete(self,request,pk):
        mark=Mark.objects.get(idMark=pk)
        mark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
