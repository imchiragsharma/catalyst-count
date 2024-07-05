from django import forms
from django.core.validators import FileExtensionValidator

class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        validators=[FileExtensionValidator(allowed_extensions=['csv'])]
    )
    

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # 2GB limit (2 * 1024 * 1024 * 1024 bytes)
            if file.size > 2 * 1024 * 1024 * 1024:
                raise forms.ValidationError("File size must be under 2 GB.")
            
            # You can add more custom validations here
            # For example, checking the file's content type
            content_type = file.content_type
            if content_type not in ['text/csv']:
                raise forms.ValidationError("Only CSV is allowed.")

        return file