from django import forms
from destination.models import BlogPost

# define here now

class CreateDestinationForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']

class UpdateDestinationForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']
    
    def save(self, commit=True):
        campsites = self.instance
        campsites.title = self.cleaned_data['title']
        campsites.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            campsites.image = self.cleaned_data['image']
        if commit:
            campsites.save()
        return campsites
