"""
URL configuration for internback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", include("person.urls")),
    path("login/", include("person.urls")),
    path("detail/", include("person.urls")),
    path("upload/", include("person.urls")),
    path("update-biography/", include("person.urls")),
    path("user-detail/", include("person.urls")),
    path("experiences/", include("experience.urls")),
    path("experience-list/", include("experience.urls")),
    path("skill/", include("skill.urls")),
    path("skill-list/", include("skill.urls")),
    path("skill/<int:pk>/", include("skill.urls")),
    path("experiences/<int:pk>/", include("experience.urls")),
    path("experiences/<int:pk>/", include("experience.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
