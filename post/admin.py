from django.contrib import admin
from .models import Post, Comment
# Register your models here.
#class DatacenterAdmin(admin.ModelAdmin):
    #list_display = ['id', 'dc_name', 'zone', 'networks', 'update_time']
    #search_fields = ['dc_name', 'zone', 'networks']
    #list_filter = ['dc_name', 'zone']
    #ordering = ['networks', 'zone']
#admin.site.register(models.Datacenter, DatacenterAdmin)#

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pub_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

