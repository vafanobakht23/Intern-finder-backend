from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import EnrollmentViewSet

router = DefaultRouter()
router.register(r"create-enrollment", EnrollmentViewSet, basename="create-enrollment")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "create-enrollment",
        EnrollmentViewSet.as_view({"post": "create"}),
        name="create-enrollment",
    ),
]
