from django.urls import path, include

app_name = "siswa"

urlpatterns = [
    path("api/", include("academics.siswa.api.urls", namespace="siswa_api")),
    path("htmx/", include("academics.siswa.htmx.urls", namespace="siswa_htmx")),
    path("", include("academics.siswa.web.urls", namespace="siswa_web")),
]