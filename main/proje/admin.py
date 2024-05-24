from django.contrib import admin
from .models import Proje,ProjeResim,ProjeAçıklama
from main.admin import admin_site
from .forms import FileFieldForm
from django.utils.html import format_html
from django import forms
from PIL import Image as PILImage
from django.http import HttpResponseRedirect


class ImageInline(admin.TabularInline):
    model = ProjeResim
    fields = ['image', 'img_preview', 'rotate_right_button',]
    readonly_fields = ['img_preview','rotate_right_button',]
    extra = 0

    def img_preview(self, obj):
        return format_html('<img src="{}" width="200" height="200" id="img-preview-{}"/>', obj.image.url, obj.pk)
    img_preview.short_description = "Image Preview"

    def rotate_image(self, obj, degrees):
        print("obje şu",obj)
        print("degreeee",degrees)
        pil_image = PILImage.open(obj.image.path)
        pil_image = pil_image.convert('RGB')
        rotated_image = pil_image.rotate(degrees, expand=True)
        rotated_image.save(obj.image.path)
        print("save edildi")

    def rotate_right_button(self, obj):
        return format_html('<input type="button" value="Döndür" onclick="rotateImage({0}, 90)">', obj.pk)
    rotate_right_button.short_description = "Döndür"

class ProjeAdmin(admin.ModelAdmin):
    form = FileFieldForm
    inlines = [ImageInline]
    list_display=['ad','eklenme_tarihi']
    exclude = ('baslik',)
    add_fieldsets = (
    (None, {
        'fields': ('ad', 'aciklama', 'ozet', 'kategori'),
    }),
    )
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)

    class Media:
        js = ['js/image_rotation.js']
class ProjeAçıklamaAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['tanim',]
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
    
    

admin.site.register(Proje, ProjeAdmin)
admin.site.register(ProjeAçıklama, ProjeAçıklamaAdmin)
ProjeAçıklama._meta.verbose_name_plural = "Açıklama"
Proje._meta.verbose_name_plural = "Projeler"
ProjeResim._meta.verbose_name_plural = "Proje Resimleri"
