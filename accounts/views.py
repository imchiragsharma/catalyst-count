from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/upload/')  # Redirect to upload page after login
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')
