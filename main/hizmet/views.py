from django.shortcuts import render
from .models import Hizmet
from hesap.models import Hesap

def service_detail_page(request,service_name):
    services=Hizmet.objects.all()
    service=Hizmet.objects.get(baslik=service_name)
    hesaplar=Hesap.objects.all()
    context={'service':service,
             'services':services,
             'hesaplar':hesaplar
            }
    return render(request,'service-details.html',context=context)