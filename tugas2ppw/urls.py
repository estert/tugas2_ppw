"""tugas2ppw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import app_mahasiswa.urls as app_mahasiswa
import app_authentication.urls as app_auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(app_auth,namespace='app-auth')),
    url(r'^mahasiswa/', include(app_mahasiswa,namespace='app-mahasiswa'))
]
