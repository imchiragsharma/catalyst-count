# data/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .utils import process_csv
# import logging

# logger = logging.getLogger(__name__)

@login_required
def upload_view(request):
    # logger.info("Upload view called")
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                process_csv(file)
                # logger.info("CSV processed successfully")
                return JsonResponse({'message': 'File uploaded and processed successfully'})
            except Exception as e:
                # logger.error(f"Error processing CSV: {e}")
                return JsonResponse({'error': str(e)}, status=400)
        else:
            # logger.error(f"Form errors: {form.errors}")
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = UploadFileForm()
    return render(request, 'data/upload.html', {'form': form})
