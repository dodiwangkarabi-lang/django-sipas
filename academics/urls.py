from django.urls import path, include

from . import views

app_name = "academics"

urlpatterns = [
    path("api/", include("academics.api.urls", namespace="academics_api")),
    path("siswa/", include("academics.siswa.urls", namespace="siswa")),
    path("kehadiran/", include("academics.kehadiran.urls", namespace="kehadiran")),
    path("akademik/", include("academics.akademik.urls", namespace="akademik")),
    path("", views.index, name="index"),
]
