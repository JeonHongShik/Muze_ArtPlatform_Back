from django.urls import path
from .views import ConsumList, ConsumDetail

urlpatterns = [
    path("", ConsumList.as_view(), name="consum_list"),
    path("<int:pk>/", ConsumDetail.as_view(), name="consum_detail"),
]
