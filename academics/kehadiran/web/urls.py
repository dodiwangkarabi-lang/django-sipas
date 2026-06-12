from django.urls import path

from . import views

app_name = "kehadiran_web"

urlpatterns = [
    path("<int:siswa_id>/create/", views.create, name="create"),
    path("<int:kehadiran_id>/", views.detail, name="detail"),
    path("", views.index, name="index"),
]