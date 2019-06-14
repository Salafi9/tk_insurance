from django.conf.urls import url
from .views import (homeView, aboutView, privacyView, termsView,
                    helpView
                )
                
urlpatterns = [
    url(r'about/', aboutView, name='about'),
    url(r'privacy/', privacyView, name='privacy'),
    url(r'terms/', termsView, name='terms'),
    url(r'home/', homeView, name='home'),
    url(r'help/', helpView, name='help'),
    url(r'', homeView, name='me'),
    ]
    
