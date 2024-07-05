# data/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# @login_required
def upload_view(request):
    if request.method == 'POST':
        # Handle file upload here
        uploaded_file = request.FILES['file']
        # Save the file or process it as needed
        # Add any logic to handle chunked uploads if necessary
        # For example, you can save the file to a temporary location
        with open(uploaded_file.name, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return render(request, 'data/upload.html', {'success': 'File uploaded successfully'})
    return render(request, 'data/upload.html')


