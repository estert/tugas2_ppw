from django.conf.urls import url
from .views import index, login
from .custom_auth import auth_login, auth_logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),

    # custom auth
    url(r'^custom_auth/login/$', auth_login, name='auth_login'),
    url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),
]
