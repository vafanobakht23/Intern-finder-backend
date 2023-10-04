from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    EnrollmentViewSet,
    EnrollmentPerUserViewSet,
    CombinedEnrollmentListView,
    CombinedEnrollmentPersonListView,
)

router = DefaultRouter()
router.register(r"create-enrollment", EnrollmentViewSet, basename="create-enrollment")
# router.register(
#     r"user-enrollment", EnrollmentPerUserViewSet, basename="user-enrollment"
# )
# router.register(r"user-enrollment", EnrollmentPerUserViewSet, basename="enrollment")
router.register(r"user-enrollment", CombinedEnrollmentListView, basename="enrollment")
router.register(
    r"post-user-enrollment", CombinedEnrollmentPersonListView, basename="enrollment"
)

urlpatterns = [
    # path("user-enrollment", include(router.urls)),
    path(
        "create-enrollment",
        EnrollmentViewSet.as_view({"post": "create"}),
        name="create-enrollment",
    ),
    path(
        "update-enrollment/<int:pk>/",
        EnrollmentViewSet.as_view({"patch": "update"}),
        name="update-enrollment",
    ),
    path("", include(router.urls)),
]
