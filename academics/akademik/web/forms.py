from django import forms

# models
from academics.models import DataAkademik

class DataAkademikForm(forms.ModelForm):
    class Meta:
        model = DataAkademik
        fields = ["nilai_tugas", "nilai_uts", "nilai_uas", "rata_rata_semester_sebelumnya", "jumlah_mata_pelajaran_lulus"]