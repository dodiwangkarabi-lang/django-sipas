import pandas as pd


class DataBuilderService:

    def build(self, siswa):
        siswa_data = self._get_siswa_data(siswa)
        academic_data = self._get_academic_data(siswa)
        attendance_data = self._get_attendance_data(siswa)

        row = {
            **siswa_data,
            **academic_data,
            **attendance_data,
        }

        return pd.DataFrame([row])

    def _get_siswa_data(self, siswa):
        return {
            "siswa_id": siswa.id,
            "nama": siswa.nama,
        }

    def _get_academic_data(self, siswa):
        return {
            "nilai_tugas": siswa.data_akademik.nilai_tugas,
            "nilai_uts": siswa.data_akademik.nilai_uts,
            "nilai_uas": siswa.data_akademik.nilai_uas,
            "rata_rata_semester_sebelumnya":
                siswa.data_akademik.rata_rata_semester_sebelumnya,
            "jumlah_mata_pelajaran_lulus":
                siswa.data_akademik.jumlah_mata_pelajaran_lulus,
        }

    def _get_attendance_data(self, siswa):
        return {
            "jumlah_izin": siswa.kehadiran.jumlah_izin,
            "jumlah_sakit": siswa.kehadiran.jumlah_sakit,
            "jumlah_alfa": siswa.kehadiran.jumlah_alfa,
        }