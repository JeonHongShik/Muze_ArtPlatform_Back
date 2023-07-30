from datetime import datetime
from django.db import models
from account.models import User


class ConsumUser(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="consum_user"
    )

    age = models.PositiveIntegerField(blank=False, null=False, default=17)  # 나이

    education = models.CharField(max_length=254)  # 학력

    career = models.CharField(max_length=254)  # 경력

    award = models.CharField(max_length=254)  # 수상수력

    introduce = models.CharField(max_length=254)  # 자기소개서

    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)
