from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def query_builder_view(request):
    return render(request, 'query_builder/query_builder.html')
