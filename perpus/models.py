from django.db import models

class RakBuku(models.Model):
    nama_rak = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_rak

class Penerbit(models.Model):
    nama_penerbit = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_penerbit

class Pengarang(models.Model):
    nama_pengarang = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_pengarang

class Buku(models.Model):
    judul_buku = models.CharField(max_length=100)
    rak_buku = models.ForeignKey(RakBuku, on_delete=models.CASCADE)
    penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE)
    pengarang = models.ManyToManyField(Pengarang)

    def __str__(self):
        return self.judul_buku

class Anggota(models.Model):
    nama_anggota = models.CharField(max_length=100)
    no_telepon = models.CharField(max_length=20)
    alamat = models.TextField()

    def __str__(self):
        return self.nama_anggota

class PinjamBuku(models.Model):
    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField()

    def __str__(self):
        return f"{self.anggota.nama_anggota} - {self.buku.judul_buku}"