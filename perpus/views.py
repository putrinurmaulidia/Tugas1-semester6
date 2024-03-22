from django.shortcuts import render, redirect
from .models import Anggota, Buku, PinjamBuku
from .forms import AnggotaForm, BukuForm, PinjamBukuForm

def daftar_anggota(request):
    if request.method == 'POST':
        form = AnggotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_anggota')
    else:
        form = AnggotaForm()

    anggota_list = Anggota.objects.all()
    context = {'form': form, 'anggota': Anggota.objects.all()}