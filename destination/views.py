from django.shortcuts import render, redirect, get_object_or_404
from destination.models import BlogPost
from destination.forms import CreateDestinationForm, UpdateDestinationForm
from account.models import Account

# Create your views here.

def create_destination_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('authenticate')
    
    form = CreateDestinationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateDestinationForm()

    context['form'] = form


    return render(request, "destination/create_destination.html", context)


def description_view(request, slug):

    context = {}
    campsites = get_object_or_404(BlogPost, slug=slug)
    context['campsites'] = campsites

    return render(request, 'destination/description.html',context)


def edit_description_view(request, slug):
    contet = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("authenticate")
    
    campsites = get_object_or_404(BlogPost, slug=slug)
    if request.POST:
        form = UpdateDestinationForm(request.POST or None, request.FILES or None, instance=campsites)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            campsites = obj
    form = UpdateDestinationForm(
        initial={
            "title": campsites.title,
            "body": campsites.body,
            "image":campsites.image,
        }
    )

    context['form'] = form
    return render(request, 'destination/edit_campsites', context)