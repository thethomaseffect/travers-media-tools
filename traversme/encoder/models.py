from django.db import models
from django import forms
import django_filepicker


class UploadModel(models.Model):
    # FPFileField renders as a filepicker dragdrop widget, but when accessed will
    # provide a File-like interface.
    filepicker_file = django_filepicker.models.FPFileField(upload_to='uploads')

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = UploadModel
