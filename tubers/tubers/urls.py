from django import urls
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webpages.urls')),
    path('youtubers/', include('youtubers.urls')),
    path('hiretubers/', include('hiretubers.urls')),
    path('inc/', include('inc.urls')),
    path('contact', include('contact.urls')),
    path('users/', include('users.urls')),
    path('socialaccounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
