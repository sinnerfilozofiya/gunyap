from django.contrib import admin
from django.contrib.auth.models import User, Group 

class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request,app_label=None):
        ordering = {
            'Dosya':1,
            'Kurumsal':2,
            'Proje':3,
            'Hizmet':4,
            'Kariyer':5,
            'Mesaj':6,
            'Hesap':7,
            'Users':8,
            'Slayt':9,
        }
        app_dict = super().get_app_list(request)
        sorted_apps = sorted(app_dict, key=lambda x: ordering.get(x['name'], 0))
        app_dict_sorted = {app['name']: app for app in sorted_apps}
        return list(app_dict_sorted.values())

admin_site = CustomAdminSite()
admin.site=admin_site
admin.site.site_header = "Günyap Grup"