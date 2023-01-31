from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.


@admin.register(KebeleHouse)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('hnum', 'location')
    

admin.site.register(Kebele)
admin.site.register(Resident)
admin.site.register(Address)
admin.site.register(House)
admin.site.register(Family)
admin.site.register(BusinessOwner)
admin.site.register(LocalBusiness)
admin.site.register(IDCard)
# admin.site.register(KebeleHouse)