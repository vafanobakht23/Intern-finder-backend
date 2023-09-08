from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserSkillViewSet, SkillViewSet

router = DefaultRouter()
router.register(r"skill", SkillViewSet, basename="skill")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "skill-list/",
        UserSkillViewSet.as_view({"post": "list"}),
        name="skill-list",
    ),
    path(
        "skill/",
        UserSkillViewSet.as_view({"delete": "delete"}),
        name="skill-delete",
    ),
]
