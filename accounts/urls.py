from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("api/", include("accounts.api.urls", namespace="accounts_api")),
    path("profil/", views.profil, name="profil"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.index, name="index"),
]