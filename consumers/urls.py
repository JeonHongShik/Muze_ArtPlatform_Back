from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsumList, ConsumDetail

router = DefaultRouter()
router.register('Consumer', ConsumList)

urlpatterns = [
    path('', include(router.urls)),
    path('Consumer/', ConsumList.as_view({'get': 'list', 'post': 'create'})),
    path('Consumer/<int:pk>/', ConsumDetail.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
