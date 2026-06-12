from accounts.models import Guru

from rest_framework import serializers

class GuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guru
        fields = "__all__"