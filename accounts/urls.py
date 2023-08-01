from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserList, UserDetail

router = DefaultRouter()
router.register("User", UserList)

urlpatterns = [
    path("", include(router.urls)),
    path("User/", UserList.as_view({"get": "list", "post": "create"})),
    path(
        "User/<int:pk>/",
        UserDetail.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]
