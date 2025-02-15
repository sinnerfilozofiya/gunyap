from django.contrib import admin
from .models import Dosya, DosyaTürü

# DosyaTürü admin ayarları
class DosyaTürüAdmin(admin.ModelAdmin):
    list_display = ('ad', 'adet','sene')  # Dosya türü adı ve toplam adetini görüntüle
    search_fields = ('ad',)  # Dosya türüne göre arama yapılabilmesi için
    list_filter = ('adet',)  # Adet'e göre filtreleme yapılabilmesi için

# Dosya admin ayarları
class DosyaAdmin(admin.ModelAdmin):
    list_display = ('dosya_turu', 'sirket', 'dosya_turu_sira','degisiklik_tarihi', 'degisiklik_yapan_kisi')  # Görüntülenecek alanlar
    search_fields = ('dosya_turu__ad', )  # Dosya adı, dosya türü ve müşteri adı ile arama yapılabilir
    list_filter = ('dosya_turu__ad', 'sirket')  # Dosya türüne ve müşteri adına göre filtreleme yapılabilir
    autocomplete_fields = ('dosya_turu','sirket')  # Dosya türü ve müşteri isimlerinin gösterilmesi
    exclude = ('dosya_turu_sira',) 

       # Ensure 'yuklenme_tarihi' is not readonly
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return []  # All fields editable
        return []  # Editable during obje
    # Dosya düzenleme formunda, dosya türü ve müşteri seçimlerini daha iyi yönetmek için
    fieldsets = ( 
        (None, {
            'fields': ('dosya_turu', 'dosya', 'sirket', 'yuklenme_tarihi',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if change:  # If the object is being updated
            # Check if any field has been modified
            if form.has_changed():
                obj.degisiklik_yapan_kisi = request.user  # Only update if there's a change
        else:
            obj.degisiklik_yapan_kisi = request.user  # Only update if there's a change
        super().save_model(request, obj, form, change)


# Admin'e modelleri kaydediyoruz
admin.site.register(DosyaTürü, DosyaTürüAdmin)
admin.site.register(Dosya, DosyaAdmin)
Dosya._meta.verbose_name_plural = "Dosyalar"
DosyaTürü._meta.verbose_name_plural = "Dosya Türleri"
