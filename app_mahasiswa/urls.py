from django.conf.urls import url
from .views import index
from .views_profile import *
from .views_riwayat import *
from .views_status import *
from .views_teman import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^edit-profile/$', edit_profile_page, name='edit_profile'),
    url(r'^edit-profile/add-keahlian/(?P<id_skill>[0-9]+)/(?P<id_level>[0-9]+)/$', add_keahlian_to_database, name='add_keahlian'),
    url(r'^edit-profile/delete-keahlian/(?P<id>\w{0,50})/$', delete_keahlian, name='delete_keahlian'),
    url(r'^edit-profile/save/$', save_perubahan, name='save_perubahan'),
    url(r'^add_status/$', add_status, name='add_status'),
    url(r'^delete_status/(?P<id>\w{0,50})/$', delete_status, name='delete_status'),
]
