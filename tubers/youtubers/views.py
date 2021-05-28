from django.shortcuts import get_object_or_404, render
from .models import Youtubers

# Create your views here.
def youtubers(request):
    tubers = Youtubers.objects.order_by('-created_date')
    data = {
        'tubers': tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtuber_detail(request, id):
    tuber = get_object_or_404(Youtubers, pk=id)
    data = {
        'tuber': tuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)

def search(request):
    pass


