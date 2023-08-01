from django.db import models
from django.contrib.auth.models import User
from posts.models import PerformancePost
from datetime import datetime


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmark")
    post = models.ForeignKey(
        PerformancePost, on_delete=models.CASCADE, related_name="bookmarked"
    )
    created_on = models.DateTimeField(default=datetime.now)
