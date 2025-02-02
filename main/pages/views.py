from django.shortcuts import render,redirect

from hizmet.models import Hizmet,HizmetAçıklama
from proje.models import Proje,ProjeAçıklama,ProjeResim
from slayt.models import Slayt,Slogan,SlaytAçıklama
from kurumsal.models import BizKimiz,Misyonumuz,Vizyonumuz,Belge
from hesap.models import Hesap,Telefon,Mail,Adres
from kariyer.models import KariyerAçıklama,KariyerGörsel
from dosya.models import Dosya
from .form import ContactForm,LoginForm
from mesaj.models import Mesaj
from django.core.paginator import Paginator
from django.http import JsonResponse
from PIL import Image as PILImage
from io import BytesIO
from django.db import models
import json
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.dateparse import parse_date


# def home_page(request):
#     services=Hizmet.objects.all()
#     slayts=Slayt.objects.order_by('order')
#     projects=Proje.objects.all()
#     hesaplar=Hesap.objects.all()
#     telefon = Telefon.objects.first()
#     mail=Mail.objects.first()
#     hizmet_tanim=HizmetAçıklama.objects.all().first()
#     slogan=Slogan.objects.all().first()
#     proje_tanim=ProjeAçıklama.objects.all().first()
#     slayt_tanim=SlaytAçıklama.objects.all().first()
#       adres=Adres.objects.first()
#     context={'services':services,
#              'slayts':slayts,
#              'projects':projects,
#              'hesaplar':hesaplar,
#              'hizmet_tanim':hizmet_tanim,
#              'proje_tanim':proje_tanim,
#              'slogan':slogan,
#              'slayt_tanim':slayt_tanim,
#              'telefon':telefon,
#              'mail':mail,
#               'adres':adres,
#             }
#     return render(request,'index.html',context=context)

def home_page(request):
    # Common data fetching
    services = Hizmet.objects.all()
    slayts = Slayt.objects.order_by('order')
    hesaplar = Hesap.objects.all()
    telefon = Telefon.objects.first()
    mail=Mail.objects.first()
    hizmet_tanim = HizmetAçıklama.objects.all().first()
    slogan = Slogan.objects.all().first()
    proje_tanim = ProjeAçıklama.objects.all().first()
    slayt_tanim = SlaytAçıklama.objects.all().first()

    # Retrieve the current filter from the request parameters or use '*' as a default
    current_filter = request.GET.get('current_filter', '*')

    # Filter projects based on the current filter if it's not '*'
    if current_filter != '*':
        projects_list = Proje.objects.filter(kategori__baslik=current_filter)
    else:
        projects_list = Proje.objects.all()

    # Paginator setup for projects
    paginator = Paginator(projects_list, 16)  # Display 16 projects per page, adjust number as needed
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    adres=Adres.objects.first()
    # Prepare the context with all necessary data
    context = {
        'telefon':telefon,
        'mail':mail,
        'services': services,
        'slayts': slayts,
        'projects': projects,
        'hesaplar': hesaplar,
        'hizmet_tanim': hizmet_tanim,
        'slogan': slogan,
        'proje_tanim': proje_tanim,
        'slayt_tanim': slayt_tanim,
        'current_filter': current_filter, # Include current filter in the context
        'adres':adres,
    }

    return render(request, 'index.html', context=context)


def about_page(request):
    bizkimiz=BizKimiz.objects.all().first()
    misyonumuz=Misyonumuz.objects.all().first()
    vizyonumuz=Vizyonumuz.objects.all().first()
    belgeler=Belge.objects.all()
    hesaplar=Hesap.objects.all()
    telefon = Telefon.objects.first()
    mail=Mail.objects.first()
    adres=Adres.objects.first()
    context={
             'telefon':telefon,
             'mail':mail,
             'bizkimiz':bizkimiz,
             'misyonumuz':misyonumuz,
             'vizyonumuz':vizyonumuz,
             'belgeler':belgeler,
             'hesaplar':hesaplar,
             'adres':adres
            }
    return render(request,'about.html',context=context)

def services_page(request):
    services=Hizmet.objects.all()
    hizmet_tanim=HizmetAçıklama.objects.all().first()
    hesaplar=Hesap.objects.all()
    telefon = Telefon.objects.first()
    mail=Mail.objects.first()
    adres=Adres.objects.first()
    context={'services':services,
             'telefon':telefon,
             'mail':mail,
             'hesaplar':hesaplar,
             'hizmet_tanim':hizmet_tanim,
             'adres':adres,
             }
    return render(request,'services.html',context=context)

def projects_page(request):
    # Retrieve the filter from the request parameters or use '*' as a default to indicate no filter
    current_filter = request.GET.get('current_filter', '*')
    telefon = Telefon.objects.first()
    mail=Mail.objects.first()
    # Fetch all necessary objects from the database
    services = Hizmet.objects.all()
    proje_tanim = ProjeAçıklama.objects.first()
    hesaplar = Hesap.objects.all()

    # Fetch all projects or filter by the category title if a specific filter is applied
    if current_filter != '*':
        projects_list = Proje.objects.filter(kategori__baslik=current_filter)
    else:
        projects_list = Proje.objects.all()
    projects_list=projects_list.order_by('-order')
    # Paginator setup: paginate the projects_list with 9 items per page
    paginator = Paginator(projects_list, 16)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    adres=Adres.objects.first()
    # Prepare the context with all necessary data
    context = {
        'telefon':telefon,
        'mail':mail,
        'adres':adres,
        'services': services,
        'projects': projects,
        'hesaplar': hesaplar,
        'proje_tanim': proje_tanim,
        'current_filter': current_filter  # Pass the current filter to the template
    }

    # Render the 'projects.html' template with the provided context
    return render(request, 'projects.html', context=context)









def contact_page(request):
    if request.method == 'POST':
        print("posta girdin")
        form = ContactForm(request.POST)
        if form.is_valid():
            print("forma girdin")
            # Process form data
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

            # Prepare email content
            email_subject = f'New Contact Message from {name}'
            email_message = (
                f'You have received a new message through your contact form.\n\n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Phone: {phone}\n'
                f'Subject: {subject}\n'
                f'Message:\n{message}'
            )

            # Send email
            # send_mail(
            #     subject=email_subject,
            #     message=email_message,
            #     from_email=settings.DEFAULT_FROM_EMAIL,
            #     recipient_list=settings.EMAIL_RECIPIENT_LIST,
            #     fail_silently=False,
            # )

    hesaplar = Hesap.objects.all()
    telefon = Telefon.objects.first()
    mail = Mail.objects.first()
    adres = Adres.objects.first()
    context = {
        'hesaplar': hesaplar,
        'telefon': telefon,
        'mail': mail,
        'adres': adres
    }
    return render(request, 'contact.html', context=context)




def login_page(request):
    if request.method == 'POST':
        print("posta girdin logindeki")
        form = LoginForm(request.POST)
        #print(form)
        if form.is_valid():
            print("forma girdin", form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            print("user", user)
            if user is not None:
                print("buldu mu")
                # Kullanıcı doğrulandı, oturumu açıyoruz
                login(request, user)
                return redirect('customer')  # 'customer' URL adını kendi projenize göre ayarlayın

            else:
                # Hatalı giriş, kullanıcıyı bilgilendirmek için bir mesaj ekleyebilirsiniz
                messages.error(request, 'Geçersiz kullanıcı adı veya şifre')
                return redirect('login')
        else:
            print(form.errors)  # Form hatalarını kontrol et
            # Form geçersizse bir hata mesajı gösterebilirsiniz
            messages.error(request, 'Formda hatalar var')
    else:
        form = LoginForm()  # İlk başta boş formu gösteriyoruz

    hesaplar = Hesap.objects.all()
    telefon = Telefon.objects.first()
    mail = Mail.objects.first()
    adres = Adres.objects.first()
    context = {
        'hesaplar': hesaplar,
        'telefon': telefon,
        'mail': mail,
        'adres': adres,
        'form': form
    }
    return render(request, 'login.html', context=context)








def documents_page(request):
    belgeler=Belge.objects.all()
    hesaplar=Hesap.objects.all()
    telefon = Telefon.objects.first()
    mail=Mail.objects.first()
    adres=Adres.objects.first()
    context={            
             'belgeler':belgeler,
             'hesaplar':hesaplar,
             'telefon':telefon,
             'mail':mail,
             'adres':adres
            }
    return render(request,'documents.html',context=context)

def career_page(request):
    kariyer_tanim=KariyerAçıklama.objects.all().first()
    kariyer_resmi=KariyerGörsel.objects.all().first()
    hesaplar=Hesap.objects.all()
    telefon = Telefon.objects.first()
    mail=Mail.objects.first()
    adres=Adres.objects.first()

    context={            
             'kariyer_tanim':kariyer_tanim,
             'kariyer_resmi':kariyer_resmi,
             'hesaplar':hesaplar,
             'telefon':telefon,
             'mail':mail,
             'adres':adres
            }
    return render(request,'career.html',context=context)

def rotate_image(request, proje_id,image_id):
    if request.method == 'POST':
        try:
            # Görsel nesnesini al
            request_data = json.loads(request.body)
            projectId = request_data['proje_id']
            imageId = request_data['image_id']
            gorsel = get_object_or_404(ProjeResim, pk=imageId)
            print("path",gorsel.image.url)
            pil_image = PILImage.open(gorsel.image.path)
            pil_image = pil_image.convert('RGB')
            rotated_image = pil_image.rotate(-90, expand=True)
            # Döndürülen görüntüyü kaydet
            rotated_image.save(gorsel.image.path)
            return JsonResponse({'error': 'Proje resmi bulundu.'})
        except ProjeResim.DoesNotExist:
            return JsonResponse({'error': 'Proje resmi bulunamadı.'}, status=400)
    else:
       pass


@login_required
def list_page(request):
    # Giriş yapan kullanıcıya ait dosyaları al
    user = request.user  # Giriş yapan kullanıcı
    dosyalar = Dosya.objects.filter(musteri=user)  # Kullanıcıya ait dosyalar

    # Filtreleme: Dosya adı ve yüklenme tarihi aralığı
    dosya_adi = request.GET.get('dosya_adi', '')  # Dosya adı
    daterange = request.GET.get('daterange', '')  # 'daterange' parametresini al
    baslangic_tarihi = request.GET.get('baslangic_tarihi', '')  # Başlangıç tarihi
    bitis_tarihi = request.GET.get('bitis_tarihi', '')  # Bitiş tarihi

    print("daterange", daterange)
    if dosya_adi:
        dosyalar = dosyalar.filter(ad__icontains=dosya_adi)  # Dosya adı içerenler
    if daterange:
        # Eğer daterange var ise, aralığı ayıklayıp filtrele
        start_date, end_date = daterange.split(' - ')  # Tarih aralığını ayır
        #dosyalar = dosyalar.filter(tarih__range=[start_date, end_date])  # Tarih aralığına göre filtrele

    # Dosya türlerini ve her türdeki adetleri al
    dosya_turleri_adet = Dosya.objects.filter(musteri=user).values('dosya_turu').annotate(adet=models.Count('dosya_turu'))

    # Diğer context verilerini hazırlıyoruz
    services = Hizmet.objects.all()
    hizmet_tanim = HizmetAçıklama.objects.first()
    hesaplar = Hesap.objects.all()
    telefon = Telefon.objects.first()
    mail = Mail.objects.first()
    adres = Adres.objects.first()

    context = {
        'services': services,
        'telefon': telefon,
        'mail': mail,
        'hesaplar': hesaplar,
        'hizmet_tanim': hizmet_tanim,
        'adres': adres,
        'dosyalar': dosyalar,  # Kullanıcıya ait dosyalar
        'dosya_turleri_adet': dosya_turleri_adet,  # Her dosya türündeki dosya sayısı
    }

    return render(request, 'list.html', context=context)


@login_required
def profile_page(request):
    # Giriş yapan kullanıcıya ait dosyaları al
    user = request.user  # Giriş yapan kullanıcı
    context = {
        'user': user,
    }

    return render(request, 'profile.html', context=context)