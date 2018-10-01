from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, RegistrationForm
from django.contrib import auth
from django.contrib.auth.models import User


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', context={'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('posts_list_url', page_number=1)
            else:
                return render(request, 'account/login.html', context={'form': form})


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('posts_list_url', page_number=1)
    

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/registration.html', context={'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password_1'])
            new_user.save()
            return redirect('posts_list_url', page_number=1)
        else:
            return render(request, 'account/registration.html', context={'form': form})
    
