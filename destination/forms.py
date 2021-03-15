from django import forms
from destination.models import BlogPost

# define here now

class CreateDestinationForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']