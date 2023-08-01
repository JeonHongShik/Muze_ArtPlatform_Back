from datetime import datetime
from django.db import models
from account.models import UserModel


class Consum(models.Model):
    author = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="consum_user"
    )
    call = models.CharField(max_length=254)  #

    profile = models.URLField(
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(blank=False, null=False, default=17)  # 나이

    education = models.CharField(max_length=254)  # 학력

    career = models.CharField(max_length=254)  # 경력

    award = models.CharField(max_length=254)  # 수상수력

    introduce = models.CharField(max_length=254)  # 자기소개서

    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)
