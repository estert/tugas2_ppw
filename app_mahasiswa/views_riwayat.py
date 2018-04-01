from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from.views import response

import requests

MATKUL_API      = 'https://private-e52a5-ppw2017.apiary-mock.com/riwayat'

def get_matkul():
    matkul = requests.get(MATKUL_API)
    return matkul.json()
