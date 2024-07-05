# data/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from .models import UploadedFile

@login_required
def upload_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            description = form.cleaned_data.get('description', '')
            uploaded_file = UploadedFile.objects.create(
                user=request.user, 
                file=file,
            )
            return JsonResponse({'message': 'File uploaded successfully'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = UploadFileForm()
    return render(request, 'data/upload.html', {'form': form})


