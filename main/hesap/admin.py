from django.contrib import admin
from .models import Hesap,Telefon,Mail,Adres
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin

class HesapAdmin(admin.ModelAdmin):
    
    exclude=['ad']
    list_display=['ad','baglanti']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
class TelefonAdmin(admin.ModelAdmin):
    
    list_display=['ad']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

class MailAdmin(admin.ModelAdmin):
    
    list_display=['ad']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

class AdresAdmin(admin.ModelAdmin):
    
    list_display=['ad']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
    
    
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name','last_name','is_staff','groups')}
        ),
    )


class CustomGroupAdmin(GroupAdmin):
    # Customize the fields to display in the admin form if needed
    fieldsets = (
        (None, {
            'fields': ('name', 'permissions'),
        }),
    )

    # You can also modify list display, search fields, etc.
    list_display = ('name',)
    search_fields = ('name',)

# TO DO yeni grup eklemek istersek bunu açıcaz
admin.site.register(Group, CustomGroupAdmin)

admin.site.register(Adres, AdresAdmin)
admin.site.register(Telefon, TelefonAdmin)
admin.site.register(Mail, MailAdmin)
admin.site.register(Hesap, HesapAdmin)

admin.site.register(User, CustomUserAdmin)
Mail._meta.verbose_name_plural = "Mail"
Telefon._meta.verbose_name_plural = "İletişim Numarası"
Hesap._meta.verbose_name_plural = "Sosyal Medya "
Adres._meta.verbose_name_plural = "Adres "