from django.contrib import admin
from .models import Subject
# Register your models here.
admin.site.register(Subject)
#class DatacenterAdmin(admin.ModelAdmin):
    #list_display = ['id', 'dc_name', 'zone', 'networks', 'update_time']
    #search_fields = ['dc_name', 'zone', 'networks']
    #list_filter = ['dc_name', 'zone']
    #ordering = ['networks', 'zone']
#admin.site.register(models.Datacenter, DatacenterAdmin)#