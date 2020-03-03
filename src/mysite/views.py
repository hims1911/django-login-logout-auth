from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'mysite/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            email = userObj['email']
            if not (User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username , password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like Username with same username and password exist')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html',{'form' : form})
