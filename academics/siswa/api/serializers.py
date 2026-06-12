from rest_framework import serializers

# models
from academics.models import (
    Siswa, DataAkademik, Kehadiran, PrediksiPrestasi
)

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = "__all__"
        
class DataAkademikSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAkademik
        fields = "__all__"
        
        
class KehadiranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kehadiran
        fields = "__all__"
        
        
class PrediksiPrestasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrediksiPrestasi
        fields = "__all__"