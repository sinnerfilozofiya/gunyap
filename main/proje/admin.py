from django.contrib import admin
from .models import Proje,ProjeImage
from main.admin import admin_site


class ImageInline(admin.TabularInline):
    model = ProjeImage
    extra = 0


class ProjeAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display=['ad','eklenme_tarihi']
    exclude = ('baslik',)
    

admin.site.site_header = "Melisa-Sina"
admin.site.register(Proje, ProjeAdmin)

Proje._meta.verbose_name_plural = "Projeler"
