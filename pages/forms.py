from django import forms
from .models import ImageFileModel

class ImageFileModelForm(forms.ModelForm):
    class Meta:
        model = ImageFileModel
        fields = '__all__'