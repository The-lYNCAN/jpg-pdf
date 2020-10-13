from django import forms
from convertor.models import *

class images_pdf(forms.ModelForm):
    class Meta:
        model = taking_img
        fields = ('name', 'image')