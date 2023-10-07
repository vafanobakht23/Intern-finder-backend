from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PostViewSet, PostUserViewSet, AllPostViewSet, SearchPostViewPost

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
        "post-search/",
        SearchPostViewPost.as_view({"get": "list"}),
        name="post-search",
    ),
    path(
        "post-delete/<int:pk>/",
        PostViewSet.as_view({"delete": "destroy"}),
        name="post-delete",
    ),
    path(
        "post-update/<int:pk>/",
        PostViewSet.as_view({"patch": "update"}),
        name="post-update",
    ),
    path(
        "all-post/",
        AllPostViewSet.as_view({"get": "list"}),
        name="all-post",
    ),
]
