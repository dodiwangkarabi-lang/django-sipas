from django.urls import path
from . import views

app_name = "siswa"

urlpatterns = [
    path("list/", views.siswa_list_view, name="list"),
]