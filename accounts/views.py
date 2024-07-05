from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/upload_data/upload/')  # Redirect to upload page after login
        else:
            return render(request, 'accounts/login.html', messages.warning(request, 'Invalid credentials'))
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
