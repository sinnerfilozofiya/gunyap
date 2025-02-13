from django.contrib import admin
from django.contrib.auth.models import User, Group 

class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request,app_label=None):
        ordering = {
            'Sirket':1,
            'Dosya':2,
            'Kurumsal':3,
            'Proje':4,
            'Hizmet':5,
            'Kariyer':6,
            'Mesaj':7,
            'Hesap':8,
            'Users':9,
            'Slayt':10,
        }
        app_dict = super().get_app_list(request)
        sorted_apps = sorted(app_dict, key=lambda x: ordering.get(x['name'], 0))
        app_dict_sorted = {app['name']: app for app in sorted_apps}
        return list(app_dict_sorted.values())

admin_site = CustomAdminSite()
admin.site=admin_site
admin.site.site_header = "Günyap Grup"