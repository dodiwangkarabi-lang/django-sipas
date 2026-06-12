from django.contrib import admin

# models
from accounts.models import Admin, Guru

admin.site.register(Admin)
admin.site.register(Guru)
