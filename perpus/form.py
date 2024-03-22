from django import forms
from .models import Anggota, Buku, PinjamBuku

class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = ['nama_anggota', 'no_telepon', 'alamat']

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['judul_buku', 'rak_buku', 'penerbit', 'pengarang']

class PinjamBukuForm(forms.ModelForm):
    class Meta:
        model = PinjamBuku
        fields = ['anggota', 'buku', 'tanggal_pinjam', 'tanggal_kembali']