from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('User', views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("kakaologin/", views.KakaoSignCallbackView.as_view()),
]
