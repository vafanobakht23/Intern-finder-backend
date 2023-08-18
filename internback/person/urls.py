from django.urls import path

from . import views
from .views import login

urlpatterns = [
    path('', views.signup , name="register"),
    path('login/',login.as_view(), name="login"),
    path('token', views.test_token,name="token"),
]
