from django.urls import path
from predictions.api import viewsets

app_name = "predictions_api"

urlpatterns = [
    path("latih-model/", viewsets.LatihModelView.as_view(), name="latih_model"),
    path("submit-prediksi/", viewsets.AdminPredictionView.as_view(), name="submit_prediksi"),
]