from rest_framework import generics
from django.contrib.auth.models import User
from bookmark.serializers import UserSerializer


class BookmarkListCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
