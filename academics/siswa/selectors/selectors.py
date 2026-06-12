from academics.models import Siswa

def get_all_siswa():
    return Siswa.objects.all()

def get_siswa():
    qs = Siswa.objects.all()
    return qs

def get_siswa_by_id(id):
    return Siswa.objects.get(id=id)