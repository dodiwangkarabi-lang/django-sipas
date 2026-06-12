# repositories/kehadiran_repository.py

# from predictions.models import Kehadiran
from academics.models import Kehadiran


class KehadiranRepository:
    """
    Repository untuk akses data kehadiran siswa
    Fokus: query database saja (no business logic / ML logic)
    """

    def get_all(self):
        return Kehadiran.objects.select_related("siswa").all()

    def get_by_siswa_id(self, siswa_id: int):
        return Kehadiran.objects.select_related("siswa").get(
            siswa_id=siswa_id
        )

    def filter_by_kehadiran_minimum(self, min_persen: float):
        """
        Ambil siswa dengan kehadiran minimal tertentu
        """
        return Kehadiran.objects.filter(
            persentase_kehadiran__gte=min_persen
        )

    def get_low_attendance(self, threshold: float = 75.0):
        """
        Contoh helper: siswa dengan kehadiran rendah
        Berguna untuk analisis atau preprocessing feature
        """
        return Kehadiran.objects.filter(
            persentase_kehadiran__lt=threshold
        )

    def exists_for_siswa(self, siswa_id: int) -> bool:
        return Kehadiran.objects.filter(
            siswa_id=siswa_id
        ).exists()