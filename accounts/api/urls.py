
from django.urls import path
from . import viewsets

app_name = "accounts_api"

urlpatterns = [
    path("guru/<int:guru_id>/", viewsets.GuruView.as_view(), name="guru"),
]