from django.urls import path
from . import views

app_name = "siswa"

urlpatterns = [
    path("<int:siswa_id>/delete/", views.siswa_delete_view, name="delete"),
    path("<int:siswa_id>/", views.siswa_detail_view, name="detail"),
    path("list/", views.siswa_list_view, name="list"),
    path("", views.index, name="index"),
]