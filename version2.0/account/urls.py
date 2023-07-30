from django.urls import path
from . import views

urlpatterns = [
    path("kakaologin/", views.KakaoSignCallbackView.as_view()),
]
