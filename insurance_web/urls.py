"""insurance_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url

# reset password
from django.contrib.auth.views import ( PasswordResetView, PasswordResetDoneView,
									 PasswordResetConfirmView, PasswordResetCompleteView
									 )

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('accounts/', include( ('accounts.urls', 'accounts'), namespace='accounts') ),
    path('index/', include( ('core.urls', 'core'), namespace='core') ),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^password_reset/$', PasswordResetView.as_view(template_name='accounts/reset_password_form.html', email_template_name='accounts/password_reset_email.html', subject_template_name='accounts/password_reset_subject.txt', extra_email_context={'domain':'hajjmabrur.tv'}), name='forgot_password' ),
	url(r'^password_reset/done/$', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done' ),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm' ),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'  ),


    
]
# Serve static and media files from development server
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

# to make sure we capture media files before wildcard (useful in dev env only)
urlpatterns += [ path('', include('accounts.urls') )]

admin.site.site_header = 'TK Insurance Admin'
admin.site.index_title = 'TK Insurance Admin Interface'
admin.site.site_title = 'TK Insurance'
