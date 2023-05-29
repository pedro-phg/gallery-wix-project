from django import forms
from . import models

class PictureForm(forms.ModelForm):
    class Meta:
        model = models.Picture
        fields = '__all__'
