from django.contrib import admin

# Register your models here.
from .models import Product, Images
class Image(admin.TabularInline):
    model = Images

class productAdmin(admin.ModelAdmin):
    list_tag = ['image_tag', 'title', 'quality']
    list_filter = ['category']
    readonly_fields = ('image_tag')
    inlines = [Image]

admin.site.register(Product, productAdmin)
admin.site.register(Images)

