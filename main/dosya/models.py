from django.db import models
from django.contrib.auth.models import User  # Kullanıcı modelini ekliyoruz
import os
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib import messages
from sirket.models import Sirket

# Dosya Türü Modeli
class DosyaTürü(models.Model):
    ad = models.CharField(max_length=100)  # Dosya türü adı (örneğin PDF, Excel, Word vb.)
    adet = models.IntegerField(default=0)  # Dosya türünün toplam sayısı
    sene =models.IntegerField(default=2025)

    def __str__(self):
        return f"{self.ad} ({self.sene})"  # Dosya türünü kullanıcıya göstereceğiz
    class Meta:
        verbose_name = 'Ölçüm Türü'  # Model adı
        verbose_name_plural = 'Ölçüm Türleri'  # Çoğul adı

def dosya_yolu(instance, filename):
    """
    Dosya yolunu dinamik olarak oluşturur.
    """
    # Dosya yolunun 'dosyalar/musteri_id/dosya_adi' formatında olmasını sağlarız.
    return os.path.join('dosyalar', str(instance.sirket.id), filename)

# Dosya Modeli
class Dosya(models.Model):
    dosya = models.FileField(upload_to=dosya_yolu)  # Dosya içeriği
    yuklenme_tarihi = models.DateTimeField(default=timezone.now)  # Dosyanın yüklendiği tarih
    olcum_turu = models.ForeignKey(DosyaTürü, on_delete=models.DO_NOTHING)  # Dosya türü
    sirket = models.ForeignKey(Sirket, related_name='dosyalar', on_delete=models.SET_NULL,null=True)  # Hangi kullanıcıya ait olduğu
    olcum_turu_sira = models.IntegerField(default=1)  # Bu dosyanın, o dosya türü içindeki sırası
    degisiklik_tarihi = models.DateTimeField(auto_now=True)  # Son değişiklik tarihi
    degisiklik_yapan_kisi = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Değişikliği yapan kişi (User)

    def __str__(self):
        return f"{self.olcum_turu}"

    class Meta:
        verbose_name = 'Rapor'  # Model adı
        verbose_name_plural = 'Raporlar'  # Çoğul adı
        ordering = ['-yuklenme_tarihi'] 

    def save(self, *args, **kwargs):
        request = kwargs.get('request', None)
        if not self.id: 
            if self.olcum_turu and self.sirket:
                dosya_turu_adet = self.olcum_turu.adet
                new_count = Dosya.objects.filter(olcum_turu=self.olcum_turu, sirket=self.sirket).count()
                if new_count >= dosya_turu_adet:
                    if request:
                        messages.error(request, "Bu türden ekleyeceğiniz maksimum dosya sayısını aştınız.")
                    return 
        else:
            pass
        super(Dosya, self).save(*args, **kwargs)
        files = Dosya.objects.filter(olcum_turu=self.olcum_turu, sirket=self.sirket).order_by('yuklenme_tarihi')
        for index, file in enumerate(files, start=1):
            file.olcum_turu_sira = index
            Dosya.objects.filter(id=file.id).update(olcum_turu_sira=index) 
