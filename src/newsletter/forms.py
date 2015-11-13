from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()
	

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["full_name","email"]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base,provider = email.split('@')
		domain, extension = provider.split('.')
		#if not domain == 'USC':
			#raise forms.ValidationError('Please make sure to use USC email')
		if not "edu" in email:
			raise forms.ValidationError("Please enter a valid edu email")
		return email