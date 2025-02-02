from django.db import models
from django.contrib.auth.models import User  # Kullanıcı modelini ekliyoruz
import os

# Dosya Türü Modeli
class DosyaTürü(models.Model):
    ad = models.CharField(max_length=100)  # Dosya türü adı (örneğin PDF, Excel, Word vb.)
    adet = models.IntegerField(default=0)  # Dosya türünün toplam sayısı

    def __str__(self):
        return self.ad  # Dosya türünü kullanıcıya göstereceğiz
  
def dosya_yolu(instance, filename):
    """
    Dosya yolunu dinamik olarak oluşturur.
    """
    # Dosya yolunun 'dosyalar/musteri_id/dosya_adi' formatında olmasını sağlarız.
    return os.path.join('dosyalar', str(instance.musteri.id), filename)

# Dosya Modeli
class Dosya(models.Model):
    ad = models.CharField(max_length=255)  # Dosyanın adı
    dosya = models.FileField(upload_to=dosya_yolu)  # Dosya içeriği
    yuklenme_tarihi = models.DateTimeField(auto_now_add=True)  # Dosyanın yüklendiği tarih
    dosya_turu = models.ForeignKey(DosyaTürü, on_delete=models.DO_NOTHING)  # Dosya türü
    musteri = models.ForeignKey(User, related_name='dosyalar', on_delete=models.SET_NULL,null=True)  # Hangi kullanıcıya ait olduğu
    dosya_turu_sira = models.IntegerField(default=0)  # Bu dosyanın, o dosya türü içindeki sırası

    def __str__(self):
        return f"{self.ad} - {self.dosya_turu.ad}"

    class Meta:
        ordering = ['-yuklenme_tarihi']  # Yüklenme tarihine göre sıralama

    
    def save(self, *args, **kwargs):
        # Dosyanın türü içindeki sırasını belirlemek için
        print("args", args,kwargs)
        if not self.id:  # Yeni bir dosya ekleniyorsa
            if self.dosya_turu and self.musteri:
                # Aynı dosya türüne sahip, aynı kullanıcıya ait olan dosyaların sayısını alıyoruz
                self.dosya_turu_sira = Dosya.objects.filter(dosya_turu=self.dosya_turu, musteri=self.musteri).count() + 1
        
        super(Dosya, self).save(*args, **kwargs)
