from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path("User/", views.UserListView.as_view({"get": "list"})),
    path("kakaologin/", views.KakaoSignCallbackView.as_view()),
]
