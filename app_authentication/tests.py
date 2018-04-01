from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .csui_helper import *
from .custom_auth import *
import environ

root = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env('.env')

class Tugas2AppAuthUnitTest(TestCase):
	def setUp(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")

	def test_tugas2_url_is_exist(self):
		response = Client().get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'session/home.html')

	def test_tugas2_login_url_is_exist(self):
		response = Client().get('/login/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'session/login.html')

		response = Client().get('/custom_auth/login/')
		self.assertEqual(response.status_code, 302)

	def test_tugas2_login_failed(self):
		response = self.client.post('/login/', {'username': "siapa", 'password': "saya"})
		html_response = response.content.decode('utf-8')
		self.assertIn("HALAMAN LOGIN", html_response)

	def test_tugas2_logout_url_is_exist(self):
		response = Client().get('/custom_auth/logout/')
		self.assertEqual(response.status_code, 302)

	def test_get_client_id(self):
		client_id = get_client_id()
		self.assertTrue(type(client_id), str)
		self.assertEqual(client_id, "X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG")
		
	def test_verify_id(self):
		verified = verify_user("1234567890")
		self.assertIn("error_description", verified)
		
	def test_get_data_user(self):
		access_token = '123456789'
		id = 'afk'
		data_user = get_data_user(access_token, id)
		self.assertIn("detail", data_user)
		self.assertEqual(data_user["detail"], "Authentication credentials were not provided.")

	def test_logged_in(self):
		# Not logged in
		response = self.client.get('/mahasiswa/profile/')
		self.assertEqual(response.status_code, 302)
		# Logged in
		self.client.post('/custom_auth/login/', {'username': self.username, 'password': self.password})
		response = self.client.get('/login/')
		self.assertEqual(response.status_code, 302)


