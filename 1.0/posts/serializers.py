# posts/serializers.py

from rest_framework import serializers
from .models import PerformancePost

class PerformancePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformancePost
        fields = '__all__'
