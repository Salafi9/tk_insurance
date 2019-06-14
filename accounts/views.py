from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from core.helpers import Egg
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import UserProfile
# Create your views here.
def singin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:      
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('accounts:dashboard'))            
        else:
            # Return an 'invalid login' error message.
            # return HttpResponseRedirect('/accounts/login/')
            context = {'error': True, 'msg':'Invalid Username or Password, Please Check and Try Again!!!'}
            return render(request, 'accounts/signin.html', context=context)
    else:
        context = {'error': False}
        return render(request, 'accounts/signin.html', context=context)

        
verify_msg = '''
            Dear {{USER}}, \n Follow the link to activate your account on {{DOMAIN}} \n
                {{VERIFY_LINK}}
            '''       
def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            try:
                User.objects.get(username=username)
                dup_username = True
            except:
                User.objects.get(email=email)
            dup = True
        except User.DoesNotExist:
            dup = False
            dup_username = False
        if not dup:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            name = fname + ' ' + lname
            profile = user.profile
            profile.name = name
            profile.phone_number = phone
            profile.save()
            subject = 'Account Activation on {}' .format(request.get_host() )
            verify_url = str(request.get_host())+"/accounts/verify/"+str(user.profile.uid)+'/'
            msg = verify_msg.replace('{{USER}}', username).replace('{{DOMAIN}}', request.get_host() ).replace('{{VERIFY_LINK}}', verify_url)
            from_email = 'hajjmabrur405@gmail.com'
            user_mail = email
            send_mail(subject, msg, from_email, [user_mail], fail_silently=True, )
            page = Egg
            page.title = "Registration Successful"
            page.sub_title = "Registration Successful"
            page.body = '''Hello, {{NAME}} ({{USERNAME}}) Registration Successful. <br />
            Follow the Instruction sent to your email to activate your account"
                '''.replace('{{NAME}}', name).replace('{{USERNAME}}', username)
            return render(request, 'accounts/welcome.html', {'page': page } )
        else:
            dup = True
            return render(request, 'accounts/signup.html', {'dup': dup, 'dup_username': dup_username } )
    else:
        return render(request, 'accounts/signup.html')


def verifyUserView(request, uid):
    page = Egg
    try:
        user = UserProfile.objects.get(uid=uid)
        if not user.active:
            user.active = True
            user.save()
            page.title = "Account Activation Successful"
            page.sub_title = "Account Activation Successful, You May Now Login Now"
            page.body = '''Hello, {{USERNAME}} Your Account is Successfully activated. <br />
            You may <a href="/accounts/login/">Login</a> now"
            '''.replace('{{USERNAME}}', user.user.username)
        else:
            print( user.name,  user.user.username )
            page.title = "Account Already Activated"
            page.sub_title = "Account was Already Activated, You May Now Login Now"
            page.body = '''Hello, {{USERNAME}} Your Account was Already Activated. <br />
            You may <a href="/accounts/login/">Login</a> now"
            '''.replace('{{USERNAME}}', user.user.username)
    except UserProfile.DoesNotExist:
        page.title = "Invalid Activation Link"
        page.sub_title = "Invalid Activation Link :: Link Expired"
        page.body = '''Sorry, Invalid Activation Link, User with does not exit, the may have Expired'''
    return render(request, 'accounts/welcome.html', {'page': page } )

@login_required(login_url='accounts/login' )
def dashboardView(request):
    user = request.user
    if user.profile.user_status() == 'Admin':
        return HttpResponseRedirect('/admin/')
    elif user.profile.user_status() == 'Employee':
        # return HttpResponseRedirect(reverse('accounts:employee-dashboard') )
        return HttpResponseRedirect('/admin/')
    elif user.profile.user_status() == 'Client':
        return HttpResponseRedirect(reverse('accounts:client-dashboard'))
    else:
        return HttpResponseRedirect( reverse('accounts:login') )

def clientDashboardView(request):
    user = request.user
    context = {'user':user}
    profile =  user.profile
    client = profile.client_profile
    context['profile'] = profile
    context['client'] = client
    return render(request, 'accounts/client_dashboard.html', context=context )

def employeeDashboardView(request):
    user = request.user
    context = {'user':user}
    profile =  user.profile
    employee = profile.employee_profile  
    context['profile'] = profile
    context['employee'] = employee
    return render(request, 'accounts/employee_dashboard.html', context=context )
