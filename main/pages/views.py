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

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.utils.dateparse import parse_date

from datetime import datetime
from django.utils import timezone

from sirket.models import SirketCalisan, Sirket
from django.contrib.auth import logout

def send_custom_email(subject, message, from_email, recipient_list):
    # SMTP server configuration
    smtp_server = 'mail.gunyapgrup.com.tr'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with your SMTP server port (587 for STARTTLS)
    smtp_username = 'bildirim@gunyapgrup.com.tr'  # Replace with your email address
    smtp_password = '4qVb01!4h'  # Replace with your email password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(recipient_list)
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, recipient_list, msg.as_string())
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

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


def deneme_page(request):
    # Retrieve the filter from the request parameters or use '*' as a default to indicate no filter
    telefon = Telefon.objects.first()
    mail=Mail.objects.first()
    # Fetch all necessary objects from the database
    hesaplar = Hesap.objects.all()


    # Paginator setup: paginate the projects_list with 9 items per page
    belgeler=Belge.objects.all()
    paginator = Paginator(belgeler, 10)
    page_number = request.GET.get('page')
    belgeler = paginator.get_page(page_number)
    adres=Adres.objects.first()

    
    # Prepare the context with all necessary data
    context = {
        'telefon':telefon,
        'mail':mail,
        'adres':adres,
        'hesaplar': hesaplar,
        'belgeler': belgeler
    }

    # Render the 'projects.html' template with the provided context
    return render(request, 'new_documents.html', context=context)


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
            email_subject = f'{name} kişisinden yeni iletişim mesajı'
            email_message = (
                f'İletişim formunuz aracılığıyla yeni bir mesaj aldınız.\n\n'
                f'İsim: {name}\n'
                f'E-posta: {email}\n'
                f'Telefon: {phone}\n'
                f'Konu: {subject}\n'
                f'Mesaj:\n{message}'
            )

            # Send email
            send_custom_email(
                subject=email_subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=settings.EMAIL_RECIPIENT_LIST
            )

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
        form = LoginForm(request.POST)
        #print(form)
        if form.is_valid():
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
    projects = Proje.objects.all()
    context={            
             'belgeler':belgeler,
             'hesaplar':hesaplar,
             'telefon':telefon,
             'mail':mail,
             'adres':adres,
             'projects':projects
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
    try:
        user=SirketCalisan.objects.filter(calisan=request.user)[0]
        sirketler=Sirket.objects.filter(calisanlar=request.user)
        sirket_id = request.GET.get('company_id', '')
        if sirket_id: 
            try:
                aktif_sirket = sirketler.get(id=sirket_id)
            except Sirket.DoesNotExist:
                aktif_sirket = sirketler.first()  # yoksa fallback
        else:  
            aktif_sirket = sirketler.first()
        dosyalar = Dosya.objects.filter(sirket=aktif_sirket) 
        dosya_turleri_adet = dosyalar.values('olcum_turu').annotate(adet=models.Count('olcum_turu'))
        context={
            "user":request.user,
            "sirket":user.sirket,
            "aktif_sirket": aktif_sirket,
            "sirketler":sirketler,
            "dosyalar":dosyalar,
            "dosya_turleri":dosya_turleri_adet
            }
        return render(request, 'list.html', context=context)
    except SirketCalisan.DoesNotExist:
        # Eğer eşleşen kullanıcı bulunmazsa, logout yap ve login sayfasına yönlendir
        print(f"Kullanıcı {request.user} için eşleşen SirketCalisan kaydı bulunamadı.")
        logout(request)  # Kullanıcıyı çıkış yap
        return redirect('/kullanici')  #


def filter_file(request):
    # user = SirketCalisan.objects.get(calisan=request.user)
    # dosyalar = Dosya.objects.filter(sirket=user.sirket)  # Kullanıcıya ait dosyalar
    sirket_id = request.GET.get('sirket_id', '')
    sirket = Sirket.objects.get(id=sirket_id)
    dosyalar = Dosya.objects.filter(sirket=sirket)
    dosya_adi = request.GET.get('dosya_adi', '').strip()  # Dosya adı filtre parametresi
    daterange = request.GET.get('daterange', '').strip()  # Tarih aralığı filtre parametresi
    start_date = None
    end_date = None

    if daterange:
        try:
            # Tarih aralığını "DD.MM.YYYY - DD.MM.YYYY" formatında parse ediyoruz
            start_date_str, end_date_str = daterange.split(' - ')
            start_date = datetime.strptime(start_date_str, '%d.%m.%Y')
            end_date = datetime.strptime(end_date_str, '%d.%m.%Y')
        except ValueError:
            pass  # Hatalı tarih formatı durumunda tarih aralığını dikkate almayacağız

    # Eğer dosya adı varsa, dosya adını filtrele
    if dosya_adi:
        dosyalar = dosyalar.filter(olcum_turu__ad__icontains=dosya_adi)

    # Eğer tarih aralığı varsa, tarih aralığını filtrele
    if start_date and end_date:
        end_date = datetime.combine(end_date, datetime.max.time())  # Bu, saat 23:59:59'a ayarlayacaktır
        dosyalar = dosyalar.filter(yuklenme_tarihi__range=[start_date, end_date])

    # dosya_turleri_adet = Dosya.objects.filter(musteri=user).values('dosya_turu').annotate(adet=models.Count('dosya_turu'))
    dosyalar_data = []
    for dosya in dosyalar:
        if dosya.yuklenme_tarihi:
            dosya_tarihi_local = dosya.yuklenme_tarihi.astimezone(timezone.get_current_timezone())
        else:
            dosya_tarihi_local = dosya.yuklenme_tarihi
        dosyalar_data.append({
            'dosya_url': dosya.dosya.url,
            'dosya_turu_sira': dosya.olcum_turu_sira,
            'dosya_turu_adet': dosya.olcum_turu.adet,
            'dosya_turu_ad': dosya.olcum_turu.ad,
            'yuklenme_tarihi': dosya_tarihi_local.strftime('%d.%m.%Y'),
        })
    return JsonResponse({'dosyalar_data': dosyalar_data})
@login_required
def profile_page(request):
    # Giriş yapan kullanıcıya ait dosyaları al
    user = request.user  # Giriş yapan kullanıcı
    context = {
        'user': user,
    }

    return render(request, 'profile.html', context=context)
