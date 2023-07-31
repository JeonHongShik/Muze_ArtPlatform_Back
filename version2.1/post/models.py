# posts/models.py
# 공연정보 게시판

from django.db import models
from datetime import datetime
from account.models import UserModel


class PerformancePost(models.Model):
    author = models.ForeignKey(
    UserModel, on_delete=models.CASCADE, related_name="Post_author")

    title = models.CharField(max_length=200)             # 포스트 제목
    
    info = models.TextField()                            # 무대정보
    type = models.CharField(max_length=50)               # 공연종류
    deadline = models.DateTimeField()                    # 모집기한
    date = models.DateTimeField()                        # 공연일시
    location = models.CharField(max_length=300)          # 공연장소
    # post_image = models.ImageField(upload_to='media/venue_images/') # 공연장 사진
    intro = models.TextField()                           # 공연소개글

    Created = models.DateTimeField(default=datetime.now)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
