from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Insurance, InsuranceType
# Create your views here.

class InsuranceView(ListView):
    template_name = "insurance/insurance_list.html"
    model = InsuranceType
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context