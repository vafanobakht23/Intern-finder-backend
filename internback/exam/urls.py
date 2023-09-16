from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ExamViewSet, ExamListViewSet

router = DefaultRouter()
router.register(r"create-exam", ExamViewSet, basename="create-exam")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "exam-list/",
        ExamListViewSet.as_view(),
        name="exam-list",
    ),
    path(
        "exam-delete/<int:pk>/",
        ExamViewSet.as_view({"delete": "destroy"}),
        name="exam-delete",
    ),
    path(
        "exam-update/<int:pk>/",
        ExamViewSet.as_view({"patch": "update"}),
        name="exam-update",
    ),
]
