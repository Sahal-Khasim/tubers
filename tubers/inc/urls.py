from django.urls.conf import path

from . import views


urlpatterns = [
    path('inc/', views.inc, name='inc'),
]