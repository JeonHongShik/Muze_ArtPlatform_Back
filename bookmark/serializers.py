from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import PerformancePost
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "date_joined"]


class PerformancePostBookmarkSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Bookmark
        fields = ["post", "user", "created_on"]

    def create(self, validated_data):
        request = self.context["request"]
        ModelClass = self.Meta.model

        instance = ModelClass.objects.create(**validated_data, **{"user": request.user})
        return instance
