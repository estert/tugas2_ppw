from django.db import models

# Create your models here.
class Pengguna(models.Model):
    kode_identitas = models.CharField('npm', max_length=20, primary_key=True, )
    nama = models.CharField('nama', max_length=200, default = 'kosong')
    username = models.CharField('username', max_length=200, default = 'kosong')
    profile_linkedin = models.CharField('profile_linkedin', max_length=200, default = 'kosong')
    foto_profil = models.CharField('profpic', max_length = 240, default = 'http://voice4thought.org/wp-content/uploads/2016/08/default1.jpg')
    email = models.CharField('email', max_length=200, default = 'kosong')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    angkatan = models.CharField('angkatan', max_length = 5)
    boolean_rahasia = models.CharField('boolean_rahasia', max_length = 5, default = 'Tidak')

class Status(models.Model):
    status = models.TextField()
    pengguna = models.ForeignKey(Pengguna, null = True)
    created_date = models.DateTimeField(auto_now_add=True)

class Keahlian(models.Model):
    keahlian = models.CharField('keahlian', max_length = 10)
    level = models.CharField('level', max_length = 15)
    pengguna = models.ForeignKey(Pengguna, null = True)
    isSaved = models.CharField('isSaved', max_length = 5, default = 'False')
