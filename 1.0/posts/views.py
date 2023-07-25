from django.shortcuts import render
from rest_framework import generics
from .models import PerformancePost
from .serializers import PerformancePostSerializer

# Create your views here.

class PerformancePostList(generics.ListCreateAPIView):
    queryset = PerformancePost.objects.all()
    serializer_class = PerformancePostSerializer

class PerformancePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerformancePost.objects.all()
    serializer_class = PerformancePostSerializer