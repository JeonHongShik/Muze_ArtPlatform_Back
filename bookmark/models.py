from django.db import models
from django.conf import settings
from post.models import PerformancePost
from datetime import datetime


class Bookmark(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookmark"
    )  # 사용자 외래키 필드를 정의하고, 연관 이름을 "bookmark"으로 표시합니다
    post = models.ForeignKey(  # 포스트 외래키 필드를 정의합니다
        PerformancePost,
        on_delete=models.CASCADE,
        related_name="bookmarked",  # PerformancePost와 관련된 필드이며, 연관 이름은 "bookmarked"입니다
    )
    created_on = models.DateTimeField(
        default=datetime.now
    )  # 북마크가 생성된 시각을 저장하는 DateTime 필드를 정의하고, 현재 시각을 기본값으로 설정합니다
