from django.contrib import admin
from .models import Sirket,SirketCalisan


# Inline form for adding Users to the Sirket
class SirketCalisanInline(admin.TabularInline):
    model = SirketCalisan
    extra = 1  # How many empty forms to show by default
    autocomplete_fields = ['calisan']  # Allows searching users by name

# Customizing the SirketAdmin to include the inline model
class SirketAdmin(admin.ModelAdmin):
    list_display = ('ad',)
    search_fields = ('ad',)
    inlines = [SirketCalisanInline]  # Add the inline model to the admin

admin.site.register(Sirket, SirketAdmin)
Sirket._meta.verbose_name="Şirket"
SirketCalisan._meta.verbose_name="Şirket Çalışanı"
Sirket._meta.verbose_name_plural = "Şirketler"
SirketCalisan._meta.verbose_name_plural = "Şirket Çalışanları"