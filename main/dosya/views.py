from django.contrib import admin
from .models import Dosya


class DosyaAdmin(admin.ModelAdmin):
    list_display = ('ad', 'yuklenme_tarihi', 'toplam_gereken_sayi', 'sıra')  # Listelemede görülecek alanlar
    list_filter = ('yuklenme_tarihi', 'toplam_gereken_sayi')  # Filtreleme yapabileceğimiz alanlar
    search_fields = ('ad',)  # Arama yapabileceğimiz alanlar
    ordering = ['-yuklenme_tarihi']  # Varsayılan sıralama: Yüklenme tarihine göre azalan sıralama


# Admin paneline Dosya modelini kaydediyoruz
admin.site.register(Dosya, DosyaAdmin)