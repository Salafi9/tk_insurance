from django.shortcuts import render
#from .models import MainPage, SiteVerification, AdsUnit, SiteInformation
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .helpers import Egg


def homeView(request):
    pass


def aboutView(request):
    try:
        #page  = MainPage.objects.get(slug='about-us')
        context = {'page': 'page'}
        return render(request, 'core/pages.html', context=context) 
    except MainPage.DoesNotExist:
        context = {'page': Egg}
        return render(request, 'core/pages.html', context=context)   


def helpView(request):
    try:
        #page  = MainPage.objects.get(slug='help')
        context = {'page': 'page'}
        return render(request, 'core/pages.html', context=context) 
    except MainPage.DoesNotExist:
        context = {'page': Egg}
        return render(request, 'core/pages.html', context=context)  


def privacyView(request):
    try:
        #page  = MainPage.objects.get(slug='privacy')
        context = {'page': 'page'}
        return render(request, 'core/pages.html', context=context) 
    except MainPage.DoesNotExist:
        context = {'page': Egg}
        return render(request, 'core/pages.html', context=context)

def termsView(request):
    try:
        #page  = MainPage.objects.get(slug='terms')
        context = {'page': 'page'}
        return render(request, 'core/pages.html', context=context) 
    except MainPage.DoesNotExist:
        context = {'page': Egg}
        return render(request, 'core/pages.html', context=context)

