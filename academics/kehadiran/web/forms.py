from django import forms

# models
from academics.models import Kehadiran

class KehadiranForm(forms.ModelForm):
    class Meta:
        model = Kehadiran
        fields = ["persentase_kehadiran", "jumlah_izin", "jumlah_sakit", "jumlah_alfa"]