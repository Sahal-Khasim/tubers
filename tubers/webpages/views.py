
from django.shortcuts import get_object_or_404, render
from .models import Slider, Team, Aboutus, Service, ServiceCard
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
    about = get_object_or_404(Aboutus)
    data = {
        'members': members,
        'about': about,
    }
    return render(request, 'webpages/about.html', data)

def services(request):
    services = get_object_or_404(Service)
    servicecard = ServiceCard.objects.all()
    data = {
        'services': services,
        'servicecard': servicecard,
    }
    return render(request, 'webpages/services.html', data)

