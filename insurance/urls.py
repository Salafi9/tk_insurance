from django.conf.urls import url
from .views import InsuranceView

urlpatterns = [
	url(r'', InsuranceView.as_view(),  name='list'),
]