"""
URL configuration for api project.

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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/v1/registration/", include("accounts.urls")),
    path("api/v1/applications/", include("applications.urls")),
    path("api/v1/schedulers/", include("schedulers.urls")),
    path("api/v1/dependencies/", include("dependencies.urls")),
    path("api/v1/cv_generator/", include("generator_cv.urls")),
    path("api/v1/letter_generator/", include("generator_letter.urls")),
    path("api/v1/profiles/", include("profiles.urls")),
    path("api/v1/simulations/", include("simulations.urls")),
    path("api/v1/email_sender/", include("email_sender.urls")),
    path("schema/download/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
