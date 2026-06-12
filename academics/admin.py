from django.contrib import admin

# models

from academics.models import (
    DataAkademik, Kehadiran, PrediksiPrestasi, Siswa
)

admin.site.register(Siswa)
admin.site.register(DataAkademik)
admin.site.register(Kehadiran)
admin.site.register(PrediksiPrestasi)
