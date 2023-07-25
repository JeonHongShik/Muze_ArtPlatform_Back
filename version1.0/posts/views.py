from django.shortcuts import render
from .models import PerformancePost
from .serializers import PerformancePostSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class PerformancePostList(ModelViewSet):
    queryset = PerformancePost.objects.all()
    serializer_class = PerformancePostSerializer

class PerformancePostDetail(ModelViewSet):
    queryset = PerformancePost.objects.all()
    serializer_class = PerformancePostSerializer