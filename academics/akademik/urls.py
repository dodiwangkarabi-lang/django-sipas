from django.urls import path, include

app_name = "akademik"

urlpatterns = [
    path("api/", include("academics.akademik.api.urls", namespace="akademik_api")),
    path("htmx/", include("academics.akademik.htmx.urls", namespace="akademik_htmx")),
    path("", include("academics.akademik.web.urls", namespace="akademik_web")),
]