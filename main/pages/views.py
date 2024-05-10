from django.shortcuts import render

from hizmet.models import Hizmet,HizmetAçıklama
from proje.models import Proje,ProjeAçıklama
from slayt.models import Slayt,Slogan,SlaytAçıklama
from kurumsal.models import BizKimiz,Misyonumuz,Vizyonumuz,Belge
from hesap.models import Hesap
from kariyer.models import KariyerAçıklama

def home_page(request):
    services=Hizmet.objects.all()
    slayts=Slayt.objects.order_by('order')
    projects=Proje.objects.all()
    hesaplar=Hesap.objects.all()
    hizmet_tanim=HizmetAçıklama.objects.all().first()
    slogan=Slogan.objects.all().first()
    proje_tanim=ProjeAçıklama.objects.all().first()
    slayt_tanim=SlaytAçıklama.objects.all().first()
    context={'services':services,
             'slayts':slayts,
             'projects':projects,
             'hesaplar':hesaplar,
             'hizmet_tanim':hizmet_tanim,
             'proje_tanim':proje_tanim,
             'slogan':slogan,
             'slayt_tanim':slayt_tanim
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
    hizmet_tanim=HizmetAçıklama.objects.all().first()
    hesaplar=Hesap.objects.all()
    context={'services':services,
             'hesaplar':hesaplar,
             'hizmet_tanim':hizmet_tanim}
    return render(request,'services.html',context=context)

def projects_page(request):
    services=Hizmet.objects.all()
    proje_tanim=ProjeAçıklama.objects.all().first()
    projects=Proje.objects.all()
    hesaplar=Hesap.objects.all()
    context={'services':services,
             'projects':projects,
             'hesaplar':hesaplar,
             'proje_tanim':proje_tanim}
    return render(request,'projects.html',context=context)
def contact_page(request):
    hesaplar=Hesap.objects.all()
    context={'hesaplar':hesaplar
             }
    return render(request,'contact.html',context=context)

def documents_page(request):
    belgeler=Belge.objects.all()
    context={            
             'belgeler':belgeler,
            }
    return render(request,'documents.html',context=context)

def career_page(request):
    kariyer_tanim=KariyerAçıklama.objects.all().first()
    context={            
             'kariyer_tanim':kariyer_tanim,
            }
    return render(request,'career.html',context=context)