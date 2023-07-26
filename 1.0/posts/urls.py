# posts/urls.py

from django.urls import path,include
from .views import PerformancePostList, PerformancePostDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('PerformancePost', PerformancePostList)

urlpatterns = [
    path('', include(router.urls)),
    path('Post', PerformancePostList.as_view({'get': 'list', 'post': 'create'}), name='post_list'),
    path('Post/<int:pk>/', PerformancePostDetail.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post_detail')
]
