from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.

response = {'author' : "Wigo, Reza, Danang, Afkar"}

def index(request):
    if 'user_login' not in request.session.keys():
        return HttpResponseRedirect('/login/')

    return HttpResponseRedirect('/mahasiswa/profile/')
