from django import forms
from django.contrib.auth.models import User

from dilooapp.models import Critic

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password')

class CriticForm(forms.ModelForm):
	class Meta:
		model = Critic
		fields = ('user')
		