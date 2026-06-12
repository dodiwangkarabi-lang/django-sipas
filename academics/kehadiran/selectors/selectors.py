# models
from academics.models import (
    Kehadiran, Siswa
)

def get_kehadiran_by_siswa(siswa_id: int) -> Kehadiran:
    return Kehadiran.objects.get(siswa_id=siswa_id)
