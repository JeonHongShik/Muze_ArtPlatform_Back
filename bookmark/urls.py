from django.urls import path
from .views import BookmarkListCreateView

urlpatterns = [
    path("", BookmarkListCreateView.as_view(), name="bookmark_list_create"),
]
