from django.contrib.auth.models import User
from django.db import models

class Guru(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_hp = models.CharField(max_length=20, null=True, blank=True)
    nip = models.CharField(max_length=50, unique=True, null=True, blank=True)
    foto = models.ImageField(upload_to="guru/", null=True, blank=True)
    
    def __str__(self):
        return f"{self.pk} - {self.nama}"

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_hp = models.CharField(max_length=20, null=True, blank=True)