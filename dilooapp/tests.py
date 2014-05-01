from django.test import TestCase

from dilooapp.forms import  UserForm, CriticForm
# Create your tests here.
class TestForms(TestCase):
	def test_register_form(self):
		data = {'user':'hugo', 'password':'hugo'}
		form_user = UserForm(data=data)
		self.assertEquals(form.is_valid(), True)

