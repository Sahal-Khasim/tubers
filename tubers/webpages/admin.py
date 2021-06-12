from django.contrib import admin
from .models import  Slider, Team, Aboutus, Service, ServiceCard
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="50" style="border-radius: 50%;" />'.format(object.photo.url))


    list_display = ('id','myphoto','first_name','role','created_date')
    list_display_links = ('first_name',)
    search_fields = ('first_name','role')
    list_filter = ('role',)


class AboutAdmin(admin.ModelAdmin):

    def aphoto(self, object):
        return format_html('<img src="{}" width="50" style="border-radius: 10%;" />'.format(object.photo.url))

    list_display = ('aphoto',)


admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)
admin.site.register(Aboutus, AboutAdmin)
admin.site.register(Service)
admin.site.register(ServiceCard)