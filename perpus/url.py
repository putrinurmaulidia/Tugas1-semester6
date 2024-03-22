from django.urls import path
from . import views

urlpatterns = [
    path('', views.pinjam_buku, name='pinjam_buku'),
    path('daftar-anggota/', views.daftar_anggota, name='daftar_anggota'),
    path('tambah-anggota/', views.tambah_anggota, name='tambah_anggota'),
    path('ubah-anggota/<int:anggota_id>/', views.ubah_anggota, name='ubah_anggota'),
    path('hapus-anggota/<int:anggota_id>/', views.hapus_anggota, name='hapus_anggota'),
    path('daftar-buku/', views.daftar_buku, name='daftar_buku'),
    path('tambah-buku/', views.tambah_buku, name='tambah_buku'),
    path('ubah-buku/<int:buku_id>/', views.ubah_buku, name='ubah_buku'),
    path('hapus-buku/<int:buku_id>/', views.hapus_buku, name='hapus_buku'),
    path('pinjam-buku/', views.pinjam_buku, name='pinjam_buku'),
]