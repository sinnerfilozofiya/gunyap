from django.shortcuts import render

from hizmet.models import Hizmet
from proje.models import Proje
from slayt.models import Slayt
from kurumsal.models import BizKimiz,Misyonumuz,Vizyonumuz,Belge
from hesap.models import Hesap

def home_page(request):
    services=Hizmet.objects.all()
    slayts=Slayt.objects.order_by('order')
    projects=Proje.objects.all()
    hesaplar=Hesap.objects.all()
    context={'services':services,
             'slayts':slayts,
             'projects':projects,
             'hesaplar':hesaplar
            }
    return render(request,'index.html',context=context)
def about_page(request):
    bizkimiz=BizKimiz.objects.all().first()
    misyonumuz=Misyonumuz.objects.all().first()
    vizyonumuz=Vizyonumuz.objects.all().first()
    belgeler=Belge.objects.all()
    hesaplar=Hesap.objects.all()
    context={'bizkimiz':bizkimiz,
             'misyonumuz':misyonumuz,
             'vizyonumuz':vizyonumuz,
             'belgeler':belgeler,
             'hesaplar':hesaplar
            }
    return render(request,'about.html',context=context)
def services_page(request):
    services=Hizmet.objects.all()
    hesaplar=Hesap.objects.all()
    context={'services':services,
             'hesaplar':hesaplar}
    return render(request,'services.html',context=context)
def projects_page(request):
    services=Hizmet.objects.all()
    projects=Proje.objects.all()
    hesaplar=Hesap.objects.all()
    context={'services':services,
             'projects':projects,
             'hesaplar':hesaplar}
    return render(request,'projects.html',context=context)
def contact_page(request):
    hesaplar=Hesap.objects.all()
    context={'hesaplar':hesaplar
             }
    return render(request,'contact.html',context=context)

