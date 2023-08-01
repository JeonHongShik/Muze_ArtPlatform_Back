# posts/models.py
# 공연정보 게시판

from django.db import models
from datetime import datetime

class PerformancePost(models.Model):
    post_title = models.CharField(max_length=200)             # 포스트 제목
    post_info = models.TextField()                            # 무대정보
    post_type = models.CharField(max_length=50)               # 공연종류
    post_deadline = models.DateTimeField()                    # 모집기한
    post_date = models.DateTimeField()                        # 공연일시
    post_location = models.CharField(max_length=300)          # 공연장소
    post_image = models.ImageField(upload_to='about_Post/venue_images/') # 공연장 사진
    post_intro = models.TextField()                           # 공연소개글

    Created = models.DateTimeField(default=datetime.now)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
