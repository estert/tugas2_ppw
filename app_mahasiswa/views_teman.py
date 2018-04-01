from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from.views import response
from .models import Pengguna, Status, Keahlian

	