from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ExperienceViewSet

router = DefaultRouter()
router.register(r"experiences", ExperienceViewSet, basename="experiences")

urlpatterns = [
    path("", include(router.urls)),
]
