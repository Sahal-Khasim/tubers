from django.urls.conf import path

from . import views


urlpatterns = [
    path('conatact/', views.contact, name='contact'),
]