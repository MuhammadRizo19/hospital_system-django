from django import forms
from django.forms import ModelForm
from .models import Referral

class ReferralForm(forms.ModelForm):
	class Meta:
		model = Referral
		fields = ('bemor', 'birthdate', 'address', 'kasalligi','qayerga','diagnoz', 'whereas')
		labels = {
		    'bemor' : "",
		    'birthdate' : "", 
		    'address' : "",
		    'kasalligi' : "",
		    'qayerga' : "",
		    'diagnoz' : "",
		    'whereas' : "",
		}
		widgets = {
		    'bemor' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'бемор исми'}),
		    'birthdate' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'тугилган йили '}),
		    'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'яшаш манзили'}),
		    'kasalligi' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'касаллиги'}),
		    'qayerga' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'қаерга жўнатилади'}),
		    'diagnoz' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'диагнози'}),
		    'whereas' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'юборилган шифохона қаерда жойлашган'}), 
		}