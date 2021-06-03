
from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtubers

# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtubers.objects.order_by('created_date').filter(is_featured = True)
    all_youtubers = Youtubers.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'sliders': sliders,
        'featured_youtubers': featured_youtubers,
        'all_youtubers': all_youtubers,
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    members = Team.objects.all()
    data = {
        'members': members,
    }
    return render(request, 'webpages/about.html', data)

def services(request):
    return render(request, 'webpages/services.html')