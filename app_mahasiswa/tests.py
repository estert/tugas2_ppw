from django.test import TestCase
from django.test import Client
from django.urls import resolve
import environ

from .models import *
from .views import *
from .views_profile import *
from .views_riwayat import *
from .views_status import *
from .views_teman import *
from app_authentication.csui_helper import *

root = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env('.env')

class Tugas2AppMahasiswaUnitTest(TestCase):
	def test_tugas2_redirect_url_mahasiswa(self):
		response = Client().get('/mahasiswa/')
		self.assertEqual(response.status_code, 302)

		response = Client().get('/mahasiswa/profile/')
		self.assertEqual(response.status_code, 302)
		
	def test_tugas2_can_delete_keahlian(self):
		objKeahlian = Keahlian()
		objKeahlian.keahlian = "Mengaji"
		objKeahlian.level = "Dewa"
		objKeahlian.save()

		response = Client().post('/mahasiswa/edit-profile/delete-keahlian/' + str(objKeahlian.id) + '/')
		self.assertEqual(response.status_code, 302)

		deleted = Keahlian.objects.filter(keahlian="Mengaji").count()
		self.assertEqual(deleted, 0)		
	
	def setUp(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")
	
	def test_login_failed(self):
		response = self.client.post('/custom_auth/login/', {'username': "brian", 'password': "estadimas"})
		html_response = self.client.get('/login/').content.decode('utf-8')
		self.assertIn("Username atau password salah", html_response)

	def test_profile(self):
		# Not logged in
		response = self.client.get('/mahasiswa/profile/')
		self.assertEqual(response.status_code, 302)
		# Logged in
		self.client.post('/custom_auth/login/', {'username': self.username, 'password': self.password})
		response = self.client.get('/mahasiswa/profile/')
		self.assertEqual(response.status_code, 200)
	
	def test_get_access_token(self):
		username = "Muhammad Afkar"
		password = "afkganteng"
		test_1 = get_access_token(username, password)
		self.assertTrue(type(test_1), str)
		self.assertIsNone(test_1)
		self.assertRaises(Exception, get_access_token(username, password))
		test_2 = get_access_token(self.username, self.password)
		self.assertIsNotNone(test_2)

    
