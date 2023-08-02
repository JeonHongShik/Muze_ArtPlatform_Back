from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("User/", views.UserListView.as_view({"get": "list"})),
    path("kakaologin/", views.KakaoSignCallbackView.as_view()),
    ##임시로 만든 url (토큰 생성)
    # path("token/", TokenObtainPairView.as_view()),
    # path("token/refresh/", TokenRefreshView.as_view()),
]
