from django.contrib import admin
from .models import Dosya, DosyaTürü

# DosyaTürü admin ayarları
class DosyaTürüAdmin(admin.ModelAdmin):
    list_display = ('ad', 'adet')  # Dosya türü adı ve toplam adetini görüntüle
    search_fields = ('ad',)  # Dosya türüne göre arama yapılabilmesi için
    list_filter = ('adet',)  # Adet'e göre filtreleme yapılabilmesi için

# Dosya admin ayarları
class DosyaAdmin(admin.ModelAdmin):
    list_display = ('ad', 'dosya_turu', 'musteri', 'yuklenme_tarihi', 'dosya_turu_sira')  # Görüntülenecek alanlar
    search_fields = ('ad', 'dosya_turu__ad', 'musteri__username')  # Dosya adı, dosya türü ve müşteri adı ile arama yapılabilir
    list_filter = ('dosya_turu', 'musteri')  # Dosya türüne ve müşteri adına göre filtreleme yapılabilir
    autocomplete_fields = ('dosya_turu', 'musteri')  # Dosya türü ve müşteri isimlerinin gösterilmesi
    exclude = ('dosya_turu_sira',) 
    # Dosya düzenleme formunda, dosya türü ve müşteri seçimlerini daha iyi yönetmek için
    def get_readonly_fields(self, request, obj=None):
        # Eğer dosya düzenleme işlemi yapılıyorsa, dosyanın yüklendiği tarih gibi bazı alanları salt okunur yapabiliriz
        if obj:  # Eğer obj varsa, yani düzenleme yapılıyorsa
            return ['yuklenme_tarihi']  # Yüklenme tarihi sadece okunabilir olacak
        return []

# Admin'e modelleri kaydediyoruz
admin.site.register(DosyaTürü, DosyaTürüAdmin)
admin.site.register(Dosya, DosyaAdmin)
Dosya._meta.verbose_name_plural = "Dosyalar"
DosyaTürü._meta.verbose_name_plural = "Dosya Türleri"
