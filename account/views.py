from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccAuthenticateForm, AccountUpdateForm

# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)



def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect('index')

    if request.POST:
        form = AccAuthenticateForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')
    else:
        form = AccAuthenticateForm()

    context['login_form'] = form
    return render(request, 'accounts/login.html',context)
        

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial = {
                "email": request.user.email,
                "username":request.user.username,
                }
        )
    context['account_form'] = form
    return render(request, 'accounts/account.html',context)


def authenticate_view(request):
    return render(request, 'accounts/authenticate.html', {})