from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register("users", views.UserListView, basename="users")

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="user-registration"),
]
