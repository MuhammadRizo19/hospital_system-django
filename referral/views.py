from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from .forms import ReferralForm
from .models import Referral
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin 
import xlwt
import datetime
import pandas as pd

class CreateReferralView(LoginRequiredMixin, generic.CreateView):
	model = Referral
	form_class = ReferralForm
	template_name = 'referral/create_referral.html'
	login_url = 'account_login'

class ReferralDetailView(LoginRequiredMixin, generic.DetailView):
	model = Referral
	template_name = 'referral/referral_detail.html'	
	contextual_object_name = 'referral'
	login_url = 'account_login'

class ReferralListView(LoginRequiredMixin, generic.ListView):
	model = Referral
	template_name = 'referral/referral_list.html'
	contextual_object_name = 'referral_list'
	paginate_by = 5
	login_url = 'account_login'

class ReferralUpdateView(LoginRequiredMixin, generic.UpdateView):
	model = Referral
	form_class = ReferralForm
	template_name = 'referral/update_referral.html'
	contextual_object_name = 'referral'
	login_url = 'account_login'

class SearchReferralView(LoginRequiredMixin, generic.ListView):
	model = Referral
	context_object_name = 'referral_list'
	template_name = 'referral/search_referral.html'
	login_url = 'account_login'

	def get_queryset(self): 
		query = self.request.GET.get('referral')
		return Referral.objects.filter(Q(bemor__icontains=query) | Q(address__icontains=query)
		)

class ReferralDeleteView(LoginRequiredMixin, generic.DeleteView):
	model = Referral
	context_object_name = 'referral'
	template_name = 'referral/delete_referral.html'
	success_url = reverse_lazy('referral_list')
	login_url = 'account_login'

class PrintReferralView(LoginRequiredMixin, generic.DetailView):
	model = Referral
	template_name = 'referral/print_referral.html'
	contextual_object_name = 'referral'
	login_url = 'account_login'

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="yo\'llanmalar.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('referrals Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['bemor ismi','tugilgan yili', 'yashash manzili', 'kasalligi', 'qayerga', 'diagnozi', 'yuborilgan shifoxona']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Referral.objects.all().values_list('bemor', 'birthdate', 'address', 'kasalligi', 'qayerga', 'diagnoz', 'whereas')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
