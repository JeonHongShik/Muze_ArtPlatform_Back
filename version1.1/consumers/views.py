from django.shortcuts import render
from .models import ConsumUser
from .serializers import ConsumerSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ConsumList(ModelViewSet):
    queryset = ConsumUser.objects.all()
    serializer_class = ConsumerSerializer
    
class ConsumerDetail(ModelViewSet):
    queryset = ConsumUser.objects.all()
    serializer_class = ConsumerSerializer
