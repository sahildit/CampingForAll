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



# new model for comment and review for each destination post
# new one

# class NewCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'content')
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "col-sm-12"}),
#             "email": forms.TextInput(attrs={"class": "col-sm-12"}),
#             "content": forms.Textarea(attrs={"class": "form-control"}),
#         }