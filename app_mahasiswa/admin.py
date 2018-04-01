from django.contrib import admin

# Register your models here.
from .models import Status, Pengguna, Keahlian

admin.site.register(Status)
admin.site.register(Pengguna)
admin.site.register(Keahlian)
