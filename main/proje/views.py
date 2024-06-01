from django.shortcuts import render
from .models import Proje
from hesap.models import Hesap
def project_details_page(request,project_id):
    proje=Proje.objects.get(id=project_id)
    hesaplar=Hesap.objects.all()
    context={'proje':proje,
             'hesaplar':hesaplar
            }
    return render(request,'project-details.html',context=context)