from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("profile/<int:user_id>/", views.user_profile_view, name="user_profile"),
    path("profile/", views.profile_view, name="profile"),
    path("sign-up/", views.signup_view, name="sign-up"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
]
