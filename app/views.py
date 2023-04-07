from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}

    return render(request, 'topic_name.html', context=d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    # LOW=Webpage.objects.order_by('player_name')
    # LOW=Webpage.objects.order_by('-player_name')
    # LOW=Webpage.objects.order_by(Length('player_name'))
    # LOW=Webpage.objects.order_by(Length('player_name').desc())
    # LOW=Webpage.objects.filter(player_name='DSP')
    LOW=Webpage.objects.exclude(player_name='MS Dhoni')




    d={'webpages':LOW}

    return render(request, 'webpage.html', context=d)

def display_about(request):
    LOA=About.objects.all()
    LOA=About.objects.filter(date__gt='2021-10-01')


    
    d={'abouts':LOA}
    return render(request, 'about.html', context=d)
