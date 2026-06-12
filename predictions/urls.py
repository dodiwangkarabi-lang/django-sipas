from django.urls import path, include
# from . import views

app_name = "predictions"

urlpatterns = [
    path("api/", include("predictions.api.urls", namespace="predictions_api")),
    path("", include("predictions.web.urls", namespace="predictions_web")),
    # path("", views.index, name="index"),
]