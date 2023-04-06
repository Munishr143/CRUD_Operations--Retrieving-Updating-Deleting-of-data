from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}

    return render(request, 'topic_name.html', context=d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpages':LOW}

    return render(request, 'webpage.html', context=d)

def display_about(request):
    LOW=About.objects.all()
    d={'abouts':LOW}

    return render(request, 'about.html', context=d)
