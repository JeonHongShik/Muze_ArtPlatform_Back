from datetime import datetime
from django.db import models

# Create your models here.
class ConsumUser(models.Model):
    
    Age = models.PositiveIntegerField( # 나이
        blank=False,
        null=False
        )
    
    Education = models.CharField( # 학력
        max_length=254
        )
    
    Career = models.CharField( # 경력
        max_length=254
        )
    
    Award = models.CharField( # 수상수력
        max_length=254
        )
    
    Introduce = models.CharField( # 자기소개서
        max_length= 254
        )
    
    Created = models.DateTimeField(default=datetime.now)
    Updated = models.DateTimeField(auto_now=True)