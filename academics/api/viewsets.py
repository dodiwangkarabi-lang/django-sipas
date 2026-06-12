from rest_framework.viewsets import ModelViewSet

# serializers
from academics.api.serializers import (
    SiswaSerializer, DataAkademikSerializer, KehadiranSerializer, PrediksiPrestasiSerializer
)

# models
from academics.models import (
    Siswa, DataAkademik, Kehadiran, PrediksiPrestasi
)

class SiswaViewSet(ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer

class DataAkademikViewSet(ModelViewSet):
    queryset = DataAkademik.objects.all()
    serializer_class = DataAkademikSerializer

class KehadiranViewSet(ModelViewSet):
    queryset = Kehadiran.objects.all()
    serializer_class = KehadiranSerializer

class PrediksiPrestasiViewSet(ModelViewSet):
    queryset = PrediksiPrestasi.objects.all()
    serializer_class = PrediksiPrestasiSerializer