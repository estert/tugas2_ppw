from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

response = {'logged_in' : False}


def index(request):
    html = 'session/home.html'
    return render(request, html, response)

def login(request):
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('app-mahasiswa:index'))
    else:
        html = 'session/login.html'
        return render(request, html, response)
