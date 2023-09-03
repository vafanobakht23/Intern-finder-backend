from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import login,UserViewSet,PersonBiographyViewSet,PersonDetailAPIView

router = DefaultRouter()
router.register(r'update-biography', PersonBiographyViewSet, basename='update-biography')

urlpatterns = [
    path('', views.signup , name="register"),
    path('login/',login.as_view(), name="login"),
    path('token', views.test_token,name="token"),
    path('detail',UserViewSet.as_view({'get': 'retrieve'})),
    path('', include(router.urls)),
    path('user-detail/', PersonDetailAPIView.as_view(), name='user-detail'),
]
