from django.urls import path
from .views import (
	HomePageView,
	documents
	)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('documents', documents, name='documents')
]