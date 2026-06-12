from django.urls import path, include

app_name = "kehadiran"

urlpatterns = [
    path("api/", include("academics.kehadiran.api.urls", namespace="kehadiran_api")),
    path("htmx/", include("academics.kehadiran.htmx.urls", namespace="kehadiran_htmx")),
    path("", include("academics.kehadiran.web.urls", namespace="kehadiran_web")),
]