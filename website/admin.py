from django.contrib import admin
from website.models import *
admin.site.site_header='Property Website'


# Register your models here.
admin.site.register(MoreProfile)
admin.site.register(PropertyType)
admin.site.register(Location)
admin.site.register(ContactAgent)
admin.site.register(Team)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('property_name',)}