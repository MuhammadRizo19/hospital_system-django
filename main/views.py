from django.shortcuts import render
from django.views import generic
from referral.models import Referral
from recipe.models import Recipe

class HomePageView(generic.TemplateView):
	template_name = 'index.html'

def documents(request):
	numreferrals = Referral.objects.all().count()
	numrecipe = Recipe.objects.all().count()
	return render(request, 'documents.html', {'numreferral': numreferrals, 'numrecipe':numrecipe})