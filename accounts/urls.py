from django.urls import path
from . import views


urlpatterns = [
    path("", views.SignUpAPIView.as_view(), name="signup"),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("<str:username>/", views.UserProfileAPIView.as_view(), name="profile"),
]
