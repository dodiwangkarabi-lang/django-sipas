from rest_framework.views import APIView
from rest_framework.response import Response

# django message
from django.contrib import messages

# facade
from predictions.facades.prediction_facade import (
    AdminPredictionFacade, LatihModelFacade, SimpanModelFacade,
    UploadDatasetFacade
)

# models
from academics.models import (
    Siswa, PrediksiPrestasi
)
from predictions.models import ModelML

class LatihModelView(APIView):
    def post(self, request):
        form_data = request.data
        file = request.FILES["dataset"]
        metadata = {
            "contoh": "contoh"
        }
        
        # upload dataset
        result = UploadDatasetFacade.execute(file=file, metadata=metadata)
        
        # latih model
        # model = LatihModelFacade.latih()
        
        # simpan model
        # SimpanModelFacade.simpan(model)
        
        # tambahkan pesan sukses
        messages.success(request, "Model berhasil di latih")
        
        return Response({
            "message": "success",
            "success": True,
            "data": form_data
        })

class AdminPredictionView(APIView):
    def post(self, request):
        formData = request.data
        siswa_id = formData.pop("siswa_id")
        siswa = Siswa.objects.get(id=siswa_id)
        
        model = ModelML.objects.first()
        hasil_prediksi = AdminPredictionFacade.prediksi(siswa_id=siswa_id, model_id=model.id)
        
        # buat atau update tabel prediks_prestasi
        prediksi_prestasi, created = PrediksiPrestasi.objects.update_or_create(
            siswa=siswa, defaults={"hasil_prediksi": hasil_prediksi[0]}
        )
        
        data = {
            "siswa_id": siswa_id,
            "hasil_prediksi": prediksi_prestasi.hasil_prediksi,
            **formData
        }
        return Response({
            "message": "success",
            "success": True,
            "data": data
        })