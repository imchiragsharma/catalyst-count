from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class AdminUploadedFile(admin.ModelAdmin):
    pass


# Register your models here.
