from django.contrib import admin
from .models import Village, VillageShop, CustomUser, DailyChallenge, Product
from django.utils.safestring import mark_safe

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    pass

@admin.register(VillageShop)
class VillageShopAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
@admin.register(DailyChallenge)
class DailyChallengeAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_tag')
    
    def image_tag(self, obj):
        return mark_safe(f'<img src="/static/{obj.image_url}" width="150" height="150" />')
    
    image_tag.short_description = 'Image'

admin.site.register(Product, ProductAdmin)

