from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import CustomUserCreationForm

@login_required

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/users.html', {'users': users})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/users_add.html', {'form': form})
