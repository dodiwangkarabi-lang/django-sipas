# models.py
from django.db import models

class Siswa(models.Model):
    nama = models.CharField(max_length=255)
    nis = models.CharField(max_length=50, unique=True)
    
    @property
    def has_kehadiran(self):
        return hasattr(self, "kehadiran")
    
    @property
    def has_data_akademik(self):
        return hasattr(self, "data_akademik")
    
    @property
    def has_prediksi_prestasi(self):
        return hasattr(self, "prediksi_prestasi")
    
    @property
    def hasil_prediksi(self):
        if self.has_prediksi_prestasi:
            return self.prediksi_prestasi.hasil_prediksi
        else:
            return ""

    def __str__(self):
        return self.nama


class DataAkademik(models.Model):
    siswa = models.OneToOneField(
        Siswa,
        on_delete=models.CASCADE,
        related_name="data_akademik"
    )

    nilai_tugas = models.FloatField()
    nilai_uts = models.FloatField()
    nilai_uas = models.FloatField()
    rata_rata_semester_sebelumnya = models.FloatField()
    jumlah_mata_pelajaran_lulus = models.PositiveIntegerField()

    def __str__(self):
        return f"Data Akademik - {self.siswa.nama}"


class Kehadiran(models.Model):
    siswa = models.OneToOneField(
        Siswa,
        on_delete=models.CASCADE,
        related_name="kehadiran"
    )

    persentase_kehadiran = models.FloatField()
    jumlah_izin = models.PositiveIntegerField(default=0)
    jumlah_sakit = models.PositiveIntegerField(default=0)
    jumlah_alfa = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Kehadiran - {self.siswa.nama}"


class PrediksiPrestasi(models.Model):

    class KategoriPrestasi(models.TextChoices):
        TINGGI = "TINGGI", "Prestasi Tinggi"
        SEDANG = "SEDANG", "Prestasi Sedang"
        RENDAH = "RENDAH", "Prestasi Rendah"

    siswa = models.OneToOneField(
        Siswa,
        on_delete=models.CASCADE,
        related_name="prediksi_prestasi"
    )

    hasil_prediksi = models.CharField(
        max_length=20,
        choices=KategoriPrestasi.choices
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.siswa.nama} - {self.hasil_prediksi}"