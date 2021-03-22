from django import forms
from .models import Googlemap

class GooglemapModelForm(forms.ModelForm):
    class Meta:
        model = Googlemap
        fields = ('dest',)
