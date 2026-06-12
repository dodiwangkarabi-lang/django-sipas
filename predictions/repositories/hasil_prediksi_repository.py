# repositories/hasil_prediksi_repository.py

from predictions.models import HasilPrediksi


class HasilPrediksiRepository:

    def create(self, hasil):
        return HasilPrediksi.objects.create(
            hasil=hasil
        )