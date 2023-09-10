from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PostViewSet, PostUserViewSet

router = DefaultRouter()
router.register(r"create-post", PostViewSet, basename="create-post")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "post-list/",
        PostUserViewSet.as_view({"post": "list"}),
        name="post-list",
    ),
    path(
        "post-delete/<int:pk>/",
        PostViewSet.as_view({"delete": "destroy"}),
        name="post-delete",
    ),
    path(
        "post-update/",
        PostViewSet.as_view({"patch": "update"}),
        name="post-update",
    ),
]
