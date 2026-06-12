# services/dataset_builder_service.py

import numpy as np

from predictions.repositories.data_akademik_repository import DataAkademikRepository
from predictions.repositories.kehadiran_repository import KehadiranRepository


class DatasetBuilderService:
    """
    Bertugas mengubah data dari database menjadi dataset ML:
    X (features) dan y (label)
    """

    def __init__(self):
        self.akademik_repo = DataAkademikRepository()
        self.kehadiran_repo = KehadiranRepository()

    def build(self):
        # 1. Ambil data dari repository
        akademik_list = self.akademik_repo.get_all()
        kehadiran_list = self.kehadiran_repo.get_all()

        # 2. Mapping agar cepat akses (siswa_id -> data)
        akademik_map = {
            a.siswa_id: a for a in akademik_list
        }

        kehadiran_map = {
            k.siswa_id: k for k in kehadiran_list
        }

        X = []
        y = []

        # 3. Join berdasarkan siswa
        for siswa_id in akademik_map.keys():

            akademik = akademik_map.get(siswa_id)
            kehadiran = kehadiran_map.get(siswa_id)

            # skip kalau data tidak lengkap
            if not akademik or not kehadiran:
                continue

            # 4. Feature engineering
            features = [
                akademik.nilai_tugas,
                akademik.nilai_uts,
                akademik.nilai_uas,
                akademik.rata_rata_semester_sebelumnya,
                akademik.jumlah_mata_pelajaran_lulus,

                kehadiran.persentase_kehadiran,
                kehadiran.jumlah_izin,
                kehadiran.jumlah_sakit,
                kehadiran.jumlah_alfa,
            ]

            X.append(features)

            # 5. Target label (contoh)
            # misalnya: klasifikasi prestasi
            y.append(self._generate_label(akademik))

        return np.array(X), np.array(y)

    def _generate_label(self, akademik):
        """
        Contoh sederhana:
        - >= 85 : A (3)
        - >= 70 : B (2)
        - < 70  : C (1)
        """

        avg = (
            akademik.nilai_tugas +
            akademik.nilai_uts +
            akademik.nilai_uas
        ) / 3

        if avg >= 85:
            return 3
        elif avg >= 70:
            return 2
        else:
            return 1