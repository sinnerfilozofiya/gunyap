from django.shortcuts import render
from .models import Proje
from hesap.models import Hesap,Telefon,Mail
def project_details_page(request,project_id):
    proje=Proje.objects.get(id=project_id)
    hesaplar=Hesap.objects.all()
    telefon = Telefon.objects.first()
    mail=Mail.objects.first()
    context={'proje':proje,
             'hesaplar':hesaplar,
             'telefon':telefon,
             'mail':mail,
            }
    return render(request,'project-details.html',context=context)