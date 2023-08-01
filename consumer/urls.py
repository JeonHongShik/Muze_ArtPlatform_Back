from django.urls import path
from .views import ConsumList, ConsumDetail
from django.urls import include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("", ConsumList.as_view(), name="consum_list"),
    path("<int:pk>/", ConsumDetail.as_view(), name="consum_detail"),
    path("delete/<int:pk>/", ConsumDetail.as_view(), name="consum_delete"),
]
