# repositories/hasil_training_repository.py

from predictions.models import HasilTraining

class HasilTrainingRepository:

    def create(
        self,
        nama_model,
        akurasi,
        lokasi_model
    ):
        return HasilTraining.objects.create(
            nama_model=nama_model,
            akurasi=akurasi,
            lokasi_model=lokasi_model
        )