from django import forms
from django.forms import ModelForm
from .models import Recipe

class RecipeForm(forms.ModelForm):
	class Meta:
		model = Recipe
		fields = (
			'bemor', 
			'diagnoz',
			'firstrec',
			'secondrec',
			'thirdrec',
			'fourthrec',
			'fifthrec',
			'sixthrec',
			'seventhrec',
			'eightthrec',
			'ninethrec',
			'tenthrec',
			'eleventhrec',
			'twelvethrec',
			'thirdteenthrec',
			'fourteenthrec',
			'fifteenthrec',
		   )
		labels = {
		    'bemor': "", 
			'diagnoz': "",
			'firstrec': "",
			'secondrec': "",
			'thirdrec': "",
			'fourthrec': "",
			'fifthrec': "",
			'sixthrec': "",
			'seventhrec': "",
			'eightthrec': "",
			'ninethrec': "",
			'tenthrec': "",
			'eleventhrec': "",
			'twelvethrec': "",
			'thirdteenthrec': "",
			'fourteenthrec': "",
			'fifteenthrec': "",
		}
		widgets = {
		    'bemor' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'бемор исми'}),
		    'diagnoz': forms.TextInput(attrs={'class':'form-control', 'placeholder':'диагнози'}),
			'firstrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'1. '}), 
			'secondrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'2. '}),
			'thirdrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'3. '}),
			'fourthrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'4. '}),
			'fifthrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'5. '}),
			'sixthrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'6. '}),
			'seventhrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'7. '}),
			'eightthrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'8. '}),
			'ninethrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'9. '}),
			'tenthrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'10. '}),
			'eleventhrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'11. '}),
			'twelvethrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'12. '}),
			'thirdteenthrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'13. '}),
			'fourteenthrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'14. '}),
			'fifteenthrec':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'15. '}),
		}