from rest_framework.views import APIView
from rest_framework.response import Response

# models
from accounts.models import Guru

# serializers
from accounts.api.serializers import GuruSerializer

class GuruView(APIView):
    def post(self, request, guru_id):
        data = request.data
        foto = request.FILES.get('foto')
        
        guru = Guru.objects.get(id=guru_id)
        if foto:
            guru.foto = foto
        guru.nama = data.get('nama')
        guru.nip = data.get('nip')
        guru.save()
        
        content = {
            'message': 'berhasil update guru',
            "success": True,
            "data": None
        }
        return Response(content)