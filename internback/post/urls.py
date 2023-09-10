from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PostViewSet

router = DefaultRouter()
router.register(r"create-post", PostViewSet, basename="create-post")

urlpatterns = [
    path("", include(router.urls)),
    # path(
    #     "post/",
    #     UserExperienceViewSet.as_view({"post": "list"}),
    #     name="experience-list",
    # ),
    # path(
    #     "experiences/",
    #     ExperienceViewSet.as_view({"patch": "update"}),
    #     name="experience-update",
    # ),
    # path(
    #     "experiences/",
    #     ExperienceViewSet.as_view({"delete": "delete"}),
    #     name="experience-delete",
    # ),
]
