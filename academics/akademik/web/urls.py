from django.urls import path

from . import views

app_name = "akademik_web"

urlpatterns = [
    path("<int:siswa_id>/create/", views.create, name="create"),
    path("<int:id>/", views.detail, name="detail"),
    path("", views.index, name="index"),
]