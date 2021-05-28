from django.contrib import admin
from .models import Youtubers
from django.utils.html import format_html



class YtAdmin(admin.ModelAdmin):

    def photos(self, object):
        return format_html('<img src="{}" width="50" style="border-radius: 50%;" />'.format(object.photo.url))


    list_display = ('id','photos','name','subs_count','is_featured',)
    search_fields = ('name','subs_count','camera_type','is_featured')
    list_filter = ('city','camera_type','subs_count')
    list_display_links = ('id','name',)
    list_editable = ('is_featured',)



admin.site.register(Youtubers, YtAdmin)