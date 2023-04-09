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
    LOW=Webpage.objects.order_by('player_name')
    LOW=Webpage.objects.order_by('-player_name')
    LOW=Webpage.objects.order_by(Length('player_name'))
    LOW=Webpage.objects.order_by(Length('player_name').desc())
    LOW=Webpage.objects.filter(player_name='DSP')
    LOW=Webpage.objects.exclude(player_name='MS Dhoni')
    LOW=Webpage.objects.filter(player_name__startswith='D')
    LOW=Webpage.objects.filter(player_name__endswith='I')
    LOW=Webpage.objects.filter(player_name__in=('Messi', 'DSP'))
    LOW=Webpage.objects.filter(player_name__contains='s')
    LOW=Webpage.objects.filter(Email__regex=r'yahoo')



    d={'webpages':LOW}

    return render(request, 'webpage.html', context=d)

def display_about(request):
    LOA=About.objects.all()
    LOA=About.objects.filter(date__gt='2021-10-01')
    LOA=About.objects.filter(date__lt='2021-10-01')
    LOA=About.objects.filter(date__lte='2021-10-05')
    LOA=About.objects.filter(date__gte='2021-10-05')
    LOA=About.objects.filter(date__year='2021')
    LOA=About.objects.filter(date__month__gt='05')
    LOA=About.objects.filter(date__day='16')




    
    d={'abouts':LOA}
    return render(request, 'about.html', context=d)
