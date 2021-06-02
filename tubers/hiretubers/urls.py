from django.urls.conf import path

from . import views


urlpatterns = [
    path('hiretubers/', views.hiretubers, name='hiretubers'),
]