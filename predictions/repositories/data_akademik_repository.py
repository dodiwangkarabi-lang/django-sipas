# repositories/data_akademik_repository.py

# from predictions.models import DataAkademik
from academics.models import DataAkademik


class DataAkademikRepository:
    """
    Repository layer untuk akses data akademik
    (hanya query, tidak ada logic ML / business rule)
    """

    def get_all(self):
        return DataAkademik.objects.select_related("siswa").all()

    def get_by_siswa_id(self, siswa_id: int):
        return DataAkademik.objects.select_related("siswa").get(
            siswa_id=siswa_id
        )

    def filter_by_nilai_minimum(self, min_nilai: float):
        """
        Contoh optional helper query
        """
        return DataAkademik.objects.filter(
            nilai_uas__gte=min_nilai
        )

    def exists_for_siswa(self, siswa_id: int) -> bool:
        return DataAkademik.objects.filter(
            siswa_id=siswa_id
        ).exists()