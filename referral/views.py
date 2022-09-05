from django.shortcuts import render,redirect
from django.views import generic
from .forms import ReferralForm
from .models import Referral
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages

class CreateReferralView(generic.CreateView):
	model = Referral
	form_class = ReferralForm
	template_name = 'referral/create_referral.html'

class ReferralDetailView(generic.DetailView):
	model = Referral
	template_name = 'referral/referral_detail.html'	
	contextual_object_name = 'referral'

class ReferralListView(generic.ListView):
	model = Referral
	template_name = 'referral/referral_list.html'
	contextual_object_name = 'referral_list'
	paginate_by = 5

class ReferralUpdateView(generic.UpdateView):
	model = Referral
	form_class = ReferralForm
	template_name = 'referral/update_referral.html'
	contextual_object_name = 'referral'

class SearchReferralView(generic.ListView):
	model = Referral
	context_object_name = 'referral_list'
	template_name = 'referral/search_referral.html'

	def get_queryset(self): 
		query = self.request.GET.get('referral')
		return Referral.objects.filter(Q(bemor__icontains=query) | Q(address__icontains=query)
		)

class ReferralDeleteView(generic.DeleteView):
	model = Referral
	context_object_name = 'referral'
	template_name = 'referral/delete_referral.html'
	success_url = reverse_lazy('referral_list')

class PrintReferralView(generic.DetailView):
	model = Referral
	template_name = 'referral/print_referral.html'
	contextual_object_name = 'referral'