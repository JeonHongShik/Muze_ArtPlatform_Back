# posts/urls.py

from django.urls import path
from .views import PerformancePostList, PerformancePostDetail

urlpatterns = [
    path('', PerformancePostList.as_view(), name='post_list'),
    path('<int:pk>/', PerformancePostDetail.as_view(), name='post_detail')
]
