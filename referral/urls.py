from django.urls import path
from .views import (
	CreateReferralView,
	ReferralDetailView,
	ReferralListView,
	ReferralUpdateView,
	SearchReferralView,
	ReferralDeleteView,
	PrintReferralView,
	export_excel
	)

urlpatterns = [
    path('new/', CreateReferralView.as_view(), name='create_referral'),
    path('<uuid:pk>/detail', ReferralDetailView.as_view(),name='referral_detail'),
    path('referral_list/', ReferralListView.as_view(), name='referral_list'),
    path('<uuid:pk>/update', ReferralUpdateView.as_view(),name='update_referral'),
    path('search_referral/', SearchReferralView.as_view(), name='search_referral'),
    path('<uuid:pk>/delete', ReferralDeleteView.as_view(), name='delete_referral'),
    path('<uuid:pk>/print_referral/', PrintReferralView.as_view(), name='print_referral'),
    path('export_excel/', export_excel, name='export_excel'),
]
