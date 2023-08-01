
from datetime import datetime
from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model): #일반 유저
    
    Name = models.CharField(
        max_length=100
        ) # 이름
    
    Email = models.EmailField(
        max_length=254
        ) # 이메일
    
    Profile = models.ImageField(
        upload_to='about_me/profile/%Y/%m/%d',
        blank=False
        ) #프로필
    
###########################

    POST = 'PT'
    CONSUMER = 'CO'
    USE_APP = [
        (POST, 'POST'),
        (CONSUMER, 'CONSUMER'),]
    
    Use = models.CharField(
        max_length=2,choices=USE_APP,default=POST) # 사용자 종류

    Created = models.DateTimeField(default=datetime.now)
    Updated = models.DateTimeField(auto_now=True)

	