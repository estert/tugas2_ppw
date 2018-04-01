from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms import Status_Form
from .views import response
from .views_riwayat import *
from django.views.decorators.csrf import csrf_exempt

# bikin views.py buat masing" fitur di sini ya, nanti kalo mau dipake ke urls.py jangan lupa di import dulu filenya

def profile(request):
    print ("#==> profile")

    if not 'user_login' in request.session.keys():
        return HttpResponseRedirect('/login/')
    else:
        kode_identitas = request.session['kode_identitas']
        try:
            pengguna = Pengguna.objects.get(kode_identitas = kode_identitas)
            set_data_for_session(pengguna)
            list_matkul = get_matkul()
        except Exception as e:
            pengguna = Pengguna()
            pengguna.kode_identitas = kode_identitas     
            pengguna.username = request.session['user_login']       
            pengguna.save()
            set_data_for_session(pengguna)
            list_matkul = get_matkul()
        
        list_keahlian = get_my_keahlian_from_database(request)
        response['list_matkul'] = list_matkul
        response['list_keahlian'] = list_keahlian
        list_pengguna = Pengguna.objects.all()
        response['list_pengguna'] = list_pengguna
        list_skill = Keahlian.objects.all()
        response['list_skill'] = list_skill
        html = 'session/mahasiswaPage.html'
        return render(request, html, response)

def set_data_for_session(user):
    response['username'] = user.username
    response['npm'] = user.kode_identitas
    response['foto_profil'] = user.foto_profil
    response['nama'] = user.nama
    response['profile_linkedin'] = user.profile_linkedin
    response['bool'] = user.boolean_rahasia
    response['email'] = user.email
    pengguna = Pengguna.objects.filter(username=user.username)
    status = Status.objects.filter(pengguna=pengguna).order_by('-id').reverse()
    response['status'] = status
    print(status)
    response['jumlah_status'] = Status.objects.all().count()
    response['dirahasiakan'] = user.boolean_rahasia
    response['status_form'] = Status_Form

    username = user.username
    user = Pengguna.objects.get(username=username)
    print (user)
    status = Status.objects.filter(pengguna__username=username)
    print (status)
    response['foto_profil'] = user.foto_profil
    response['status'] = status
    response['status_form'] = Status_Form
    response['model'] = status

def get_my_keahlian_from_database(request):
    resp = []
    kode_identitas = request.session['kode_identitas']
    pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
    items = Keahlian.objects.filter(pengguna=pengguna)
    for item in items:
        resp.append(item)
    return resp

def edit_profile_page(request):
    if not 'user_login' in request.session:
        return HttpResponseRedirect(reverse('app-mahasiswa:index'))
    else:
        list_keahlian = get_my_keahlian_from_database(request)
        response['list_keahlian'] = list_keahlian
        kode_identitas = request.session['kode_identitas']
        pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
        set_data_for_session(pengguna)
        html = 'session/edit_profile.html'
        return render(request, html, response)

def add_keahlian_to_database(request, id_skill, id_level):
    skills = ['Java', 'C#', 'Python', 'Erlang', 'Kotlin']
    levels = ['Beginner', 'Intermediate', 'Advanced', 'Expert', 'Legend']
    kode_identitas = request.session['kode_identitas']
    pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
    objKeahlian = Keahlian()
    objKeahlian.keahlian = skills[int(id_skill)]
    objKeahlian.level = levels[int(id_level)]
    objKeahlian.pengguna = pengguna
    objKeahlian.save()
    return HttpResponseRedirect('/mahasiswa/edit-profile/')

def delete_keahlian(request, id):
    instance = Keahlian.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect('/mahasiswa/edit-profile/')

@csrf_exempt
def save_perubahan(request):
    kode_identitas = request.session['kode_identitas']
    pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
    pengguna.boolean_rahasia = request.POST['boolean_rahasia']
    pengguna.nama = request.POST['nama']
    pengguna.email = request.POST['email']
    pengguna.profile_linkedin = request.POST['linkedin_link']
    pengguna.foto_profil = request.POST['foto_profil']
    pengguna.save()
    return HttpResponseRedirect('/mahasiswa/profile/')
    



    



