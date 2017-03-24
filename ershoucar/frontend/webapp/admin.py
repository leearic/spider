from django.contrib import admin

# Register your models here.
from . models import *



class  CarTestingInline(admin.TabularInline):
    model = TestingInfoModel
    fk_name = 'car'

class  CarImagesInline(admin.TabularInline):
    model = ImageInfoModel
    fk_name = 'car'



# #
class TestingInfoModellAdmin(admin.ModelAdmin):
    list_display = ('name', 'module', 'price', 'car_address')
    list_filter = ('price', 'module', 'car_address')
    inlines = [CarTestingInline, CarImagesInline]


admin.site.register(CarinfoModel, TestingInfoModellAdmin)
#
#
# class CarInfoModelAdmin(admin.ModelAdmin):
#     list_display = ('module', 'price', 'car_address')
#     inlines = [CarInfoInline]
#
# admin.site.register(CarinfoModel, CarInfoModelAdmin)
#
#
#
#
#
#
# class carModelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'url')
#
#
# admin.site.register(CarModel, carModelAdmin)