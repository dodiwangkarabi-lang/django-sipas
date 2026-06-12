from django.urls import path
from . import views

app_name = "predictions_web"

urlpatterns = [
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path("", views.PredictionView.as_view(), name="index"),
]