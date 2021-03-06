from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-login-callback"),
    path("login/kakao", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback", views.kakao_callback, name="kakao-login-callback"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete_verification"),
    path("update-profile", views.UpdateProfile.as_view(), name="updateProfile"),
    path("update-password", views.UpdatePassword.as_view(), name="updatePassword"),
    path("hosting/", views.switch_hosting, name="hosting"),
    path("language/", views.switch_lang, name="lang"),
    path("<int:pk>/", views.ProfileView.as_view(), name="profile"),
]
