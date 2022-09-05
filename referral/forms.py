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
		    'bemor' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'bemor ismi'}),
		    'birthdate' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'tug\'ilgan yili '}),
		    'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'yashash manzili'}),
		    'kasalligi' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'kasalligi'}),
		    'qayerga' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'qayerga jo\'natiladi'}),
		    'diagnoz' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'diagnozi'}),
		    'whereas' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'shifoxona joylashuvi'}), 
		}