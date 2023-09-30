from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    login,
    UserViewSet,
    PersonViewSet,
    PersonDetailAPIView,
    FileUploadView,
    UserLogoutView,
    PersonDetailViewSet,
)

router = DefaultRouter()
router.register(r"update-biography", PersonViewSet, basename="update-biography")
# router.register(r"user-detail", PersonDetailViewSet, basename="user-detail")

urlpatterns = [
    path("", views.signup, name="register"),
    path("login/", login.as_view(), name="login"),
    path("token", views.test_token, name="token"),
    path("detail", UserViewSet.as_view({"get": "retrieve"})),
    path("user-detail", PersonDetailViewSet.as_view({"get": "retrieve"})),
    path("", include(router.urls)),
    # path("user-detail/", PersonDetailAPIView.as_view(), name="user-detail"),
    path("upload/", FileUploadView.as_view(), name="file-upload"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
