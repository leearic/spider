from django.contrib import admin

# Register your models here.

from .models import  Coser, Category, Images, Ads





class ImagesInline(admin.TabularInline):
    model = Images
    fk_name = 'coser'

class CategoryInline(admin.TabularInline):
    model = Category
    fk_name = 'coser'

# class CategoryAdmin(admin.ModelAdmin):
#     pass

class CoserAdmin(admin.ModelAdmin):
    list_display = ('title',  'istop')
    search_fields = ('title', 'istop')
    list_filter = ('istop',)

    readonly_fields = ('topimage_tag', 'addtime', 'come_from', 'topimage')
    exclude = ('topimage',)
    inlines = [ImagesInline, CategoryInline, ]



#
# class ImagesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'real_url')
#     readonly_fields = ('relate_url_tag', 'real_url_tag', 'real_url', 'relate_url')
#     exclude = ('relate_url_tag', 'real_url_tag',)
#     # inlines = [CoserInline, ]


admin.site.register(Coser, CoserAdmin)
# admin.site.register(Category, CategoryAdmin)





# admin.site.register(Images, ImagesAdmin)
admin.site.register(Ads)