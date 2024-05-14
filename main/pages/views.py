from django.shortcuts import render

from hizmet.models import Hizmet,HizmetAçıklama
from proje.models import Proje,ProjeAçıklama
from slayt.models import Slayt,Slogan,SlaytAçıklama
from kurumsal.models import BizKimiz,Misyonumuz,Vizyonumuz,Belge,Sayaç
from hesap.models import Hesap
from kariyer.models import KariyerAçıklama,KariyerGörsel
from .form import ContactForm
from mesaj.models import Mesaj
from django.core.paginator import Paginator

# def home_page(request):
#     services=Hizmet.objects.all()
#     slayts=Slayt.objects.order_by('order')
#     projects=Proje.objects.all()
#     hesaplar=Hesap.objects.all()
#     hizmet_tanim=HizmetAçıklama.objects.all().first()
#     slogan=Slogan.objects.all().first()
#     proje_tanim=ProjeAçıklama.objects.all().first()
#     slayt_tanim=SlaytAçıklama.objects.all().first()
#     context={'services':services,
#              'slayts':slayts,
#              'projects':projects,
#              'hesaplar':hesaplar,
#              'hizmet_tanim':hizmet_tanim,
#              'proje_tanim':proje_tanim,
#              'slogan':slogan,
#              'slayt_tanim':slayt_tanim
#             }
#     return render(request,'index.html',context=context)

def home_page(request):
    services = Hizmet.objects.all()
    slayts = Slayt.objects.order_by('order')
    hesaplar = Hesap.objects.all()
    hizmet_tanim = HizmetAçıklama.objects.all().first()
    slogan = Slogan.objects.all().first()
    proje_tanim = ProjeAçıklama.objects.all().first()
    slayt_tanim = SlaytAçıklama.objects.all().first()

    # Get all projects
    projects_list = Proje.objects.all()

    # Set up pagination for projects
    paginator = Paginator(projects_list, 9)  # Display 9 projects per page, adjust number as needed
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    context = {
        'services': services,
        'slayts': slayts,
        'projects': projects,  # This now contains the paginated projects
        'hesaplar': hesaplar,
        'hizmet_tanim': hizmet_tanim,
        'slogan': slogan,
        'proje_tanim': proje_tanim,
        'slayt_tanim': slayt_tanim
    }

    return render(request, 'index.html', context=context)


def about_page(request):
    bizkimiz=BizKimiz.objects.all().first()
    misyonumuz=Misyonumuz.objects.all().first()
    vizyonumuz=Vizyonumuz.objects.all().first()
    sayac=Sayaç.objects.all().first()
    belgeler=Belge.objects.all()
    hesaplar=Hesap.objects.all()
    context={'bizkimiz':bizkimiz,
             'misyonumuz':misyonumuz,
             'vizyonumuz':vizyonumuz,
             'belgeler':belgeler,
             'hesaplar':hesaplar,
             'sayac':sayac
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
    services = Hizmet.objects.all()
    proje_tanim = ProjeAçıklama.objects.all().first()
    hesaplar = Hesap.objects.all()

    # Get all projects
    projects_list = Proje.objects.all()

    # Set up pagination
    paginator = Paginator(projects_list, 9)  # Display 9 projects per page
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    # Prepare context
    context = {
        'services': services,
        'projects': projects,
        'hesaplar': hesaplar,
        'proje_tanim': proje_tanim
    }

    return render(request, 'projects.html', context=context)


def contact_page(request):
        if request.method == 'POST':
            print("posta girdin")
            form = ContactForm(request.POST)
            if form.is_valid():
                print("forma girdin")
                # Form verilerini işleyin
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                mesaj = Mesaj.objects.create(
                        gönderen=name,
                        mail=email,
                        telefon=phone,
                        konu=subject,
                        mesaj=message,
                    )
                mesaj.save()
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
    kariyer_resmi=KariyerGörsel.objects.all().first()
    context={            
             'kariyer_tanim':kariyer_tanim,
             'kariyer_resmi':kariyer_resmi
            }
    return render(request,'career.html',context=context)