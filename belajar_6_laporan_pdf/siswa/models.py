from django.db import models

# Create your models here.
class SiswaModel(models.Model):
    nama = models.CharField(max_length=250)
    kelas = models.CharField(max_length=50)
    alamat = models.CharField(max_length=250)

    def __str__(self):
        return self.nama
    