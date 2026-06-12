from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# services
from predictions.services.prediction_service import PredictionService
from predictions.services.training_service import TrainingService
from predictions.services.testing_service import TestingService

# facade
from predictions.facades.prediction_facade import AdminPredictionFacade

# models
from academics.models import (
    PrediksiPrestasi
)
from predictions.models import (
    ModelML, TrainingRun, DatasetVersion, Dataset
)

class SettingsView(View):
    def get(self, request):
        context = {}
        template_name = "predictions/pages/settings.html"
        return render(request, template_name, context)


class AdminPredictionView(View):
    def post(self, request, siswa_id):
        hasil_prediksi = AdminPredictionFacade.prediksi(siswa_id=siswa_id)
        
        # create or update 
        obj, created = PrediksiPrestasi.objects.update_or_create(
            siswa_id=siswa_id,
            defaults= {
                "hasil_prediksi": hasil_prediksi[0]
            }
        )
        
        return redirect(reverse("academics:siswa:siswa_web:detail", kwargs={"siswa_id": siswa_id}))

class PredictionView(View):
    def get(self, request):
        model_ml = get_object_or_404(ModelML, id=1)
        training_run = model_ml.training_run
        dataset_version = training_run.dataset_version
        metrics = training_run.metrics
        # konversi ke skala 100 jika nilai adalah bilangan %
        metrics = {
            k: v * 100 if isinstance(v, float) else v
            for k, v in metrics.items()
        }
        context = {
            "model": model_ml,
            "training_run": training_run,
            "dataset_version": dataset_version,
            "metrics": metrics
        }
        template_name = "predictions/pages/index.html"
        return render(request, template_name, context)
    
    def post(self, request):
        input_data = [
            float(request.POST["fitur_1"]),
            float(request.POST["fitur_2"]),
            float(request.POST["fitur_3"]),
        ]
        
        service = PredictionService()

        hasil = service.predict(
            model_path="media/models/random_forest.joblib",
            input_data=input_data
        )
        
class TrainingView(View):

    def post(self, request):
        service = TrainingService()
        x_train = request.POST["x_train"]
        y_train = request.POST["y_train"]
        x_test = request.POST["x_test"]
        y_test = request.POST["y_test"]

        hasil = service.train(
            model_name=request.POST["model"],
            x_train=x_train,
            y_train=y_train,
            x_test=x_test,
            y_test=y_test
        )

        # return JsonResponse({
        #     "id": hasil.id,
        #     "akurasi": hasil.akurasi,
        # })
        
class TestingView(View):

    template_name = "prediksi/testing_result.html"

    def get(self, request):
        service = TestingService()

        result = service.test(
            model_path="media/models/random_forest.joblib"
        )

        context = {
            "accuracy": result["accuracy"],
            "precision": result["precision"],
            "recall": result["recall"],
            "f1_score": result["f1_score"],
        }

        return render(
            request,
            self.template_name,
            context
        )