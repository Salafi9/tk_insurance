from django.conf.urls import url, include

from .views import signup, singin, verifyUserView, clientDashboardView, employeeDashboardView, dashboardView

from django.contrib.auth.views import LogoutView

urlpatterns = [
	url(r'login/$', singin,  name='login'),
	url(r'signup/$', signup, name='signup'),
	url(r'verify/(?P<uid>[0-9a-f-]+)/', verifyUserView, name='verify-user'),
	url(r'logout/$', LogoutView.as_view(), {'next_page': '/'}, name='logout'),
	url(r'dashboard/', dashboardView, name='dashboard'),
	url(r'client/$', clientDashboardView, name='client-dashboard'),
	url(r'employee/$', employeeDashboardView, name='employee-dashboard'),
	url(r'', singin),
	url('^', include('django.contrib.auth.urls')),
]
 
