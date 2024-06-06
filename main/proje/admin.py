from django.contrib import admin
from .models import Proje,ProjeResim,ProjeAçıklama
from main.admin import admin_site
from .forms import FileFieldForm
from django.utils.html import format_html
from django import forms
from PIL import Image as PILImage
from django.http import HttpResponseRedirect
from django.urls import reverse
import time

class ImageInline(admin.TabularInline):
    model = ProjeResim
    fields = ['image', 'img_preview', 'rotate_button',]
    readonly_fields = ['img_preview','rotate_button',]
    extra = 0

    def img_preview(self, obj):
            unique_param = f"?v={int(time.time())}"
            image_url = f"{obj.image.url}{unique_param}"
            return format_html('<img src="{}" width="200" height="200" id="img-preview-{}"/>', image_url, obj.pk)
    img_preview.short_description = "Image Preview"


    def rotate_button(self, obj):
       return format_html('<a class="rotate-image-button" data-image-id="{}" data-project-id="{}" data-rotate-url="{}" style="cursor: pointer;">Döndür</a>',
                   obj.pk, obj.proje.id,reverse("rotate_image", args=[obj.pk, obj.proje.id]))
    rotate_button.short_description = "Döndür"

class ProjeAdmin(admin.ModelAdmin):
    form = FileFieldForm
    inlines = [ImageInline]
    list_display=['ad','order',]
    exclude = ('baslik',)
    
    fieldsets = (
        (None, {
            'fields': ('ad', 'aciklama', 'kategori','proje_tarihi','kapak_resmi','video'),
        }),
    )
    add_fieldsets = (
    (None, {
        'fields': ('ad', 'aciklama', 'ozet', 'kategori','video'),
    }),
    )


    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)

    class Media:
        js = ('js/custom_admin.js',)
class ProjeAçıklamaAdmin(admin.ModelAdmin):
    list_display=['tanim',]
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
    
    

admin.site.register(Proje, ProjeAdmin)

Proje._meta.verbose_name_plural = "Projeler"
ProjeResim._meta.verbose_name_plural = "Proje Resimleri"
