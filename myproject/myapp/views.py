from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BlogView(APIView):
    def get(self,request):
        blog1=Blog.objects.all()
        serializer=BlogSerializer(blog1, many=True)
        return Response(serializer.data)


    def post(self):
        pass