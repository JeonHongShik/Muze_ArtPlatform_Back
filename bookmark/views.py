from rest_framework import generics
from django.contrib.auth.models import User
from bookmark.serializers import BookmarkSerializer
from .models import Bookmark


# 이 아래에서 BookmarkListCreateView를 정의합니다
class BookmarkListCreateView(
    generics.ListCreateAPIView
):  # generics.ListCreateAPIView로 수정합니다
    serializer_class = BookmarkSerializer  # 북마크를 시리얼라이즈 하기 위해 BookmarkSerializer를 사용합니다

    def get_queryset(self):  # BookmarkListCreateView 클래스 안에 get_queryset 메소드를 추가합니다
        user = self.request.user
        return Bookmark.objects.filter(user=user)
