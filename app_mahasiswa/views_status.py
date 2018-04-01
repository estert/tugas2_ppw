from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Status, Pengguna
from .forms import Status_Form

from.views import response

# bikin views.py buat masing" fitur di sini ya, nanti kalo mau dipake ke urls.py jangan lupa di import dulu filenya 

def add_status(request):
    form = Status_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['isi'] = request.POST['status']
        username = request.session['user_login']
        user = Pengguna.objects.get(username=username)
        status = Status(pengguna=user,status=response['isi'])
        status.save()
        return HttpResponseRedirect('/mahasiswa/profile/')

def delete_status(request, id):
    instance = Status.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect('/mahasiswa/profile/')
