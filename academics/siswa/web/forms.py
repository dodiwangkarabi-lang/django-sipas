# models 
from academics.models import Siswa

from django import forms


class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ["nama", "nis"]