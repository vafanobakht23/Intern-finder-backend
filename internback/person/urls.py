from django.urls import path

from . import views

urlpatterns = [
    path('', views.signup , name="register"),
    path('login/', views.login, name="login"),
    path('token', views.test_token,name="token"),
]
