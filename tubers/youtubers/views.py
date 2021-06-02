from django.shortcuts import get_object_or_404, render
from .models import Youtubers



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
    tubers = Youtubers.objects.order_by('-created_date')
    city_search = Youtubers.objects.values_list(
        'city', flat=True).distinct()
    camera_type_search = Youtubers.objects.values_list(
        'camera_type', flat=True).distinct()
    catagory_search = Youtubers.objects.values_list(
        'catagory', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)

    if 'catagory' in request.GET:
        catagory = request.GET['catagory']
        if catagory:
            tubers = tubers.filter(catagory__iexact=catagory)


    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'catagory_search': catagory_search,

    }
    return render(request, 'youtubers/search.html', data)


