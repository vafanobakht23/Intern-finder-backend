from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ExperienceViewSet, UserExperienceViewSet

router = DefaultRouter()
router.register(r"experiences", ExperienceViewSet, basename="experiences")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "experience-list/",
        UserExperienceViewSet.as_view({"post": "list"}),
        name="experience-list",
    ),
]
