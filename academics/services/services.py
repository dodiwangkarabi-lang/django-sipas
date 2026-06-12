from academics.models import (
    Siswa, Kehadiran, DataAkademik
)
from core.services.base import BaseService

class SiswaService(BaseService):
    model = Siswa
    
class KehadiranServices(BaseService):
    model = Kehadiran

class DataAkademikServices(BaseService):
    model = DataAkademik