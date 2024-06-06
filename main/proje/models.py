from django.db import models
from django.utils.text import slugify
from hizmet.models import Hizmet
from PIL import Image as PILImage
from ckeditor.fields import RichTextField

def proje_directory_path(instance,filename):
    ad=slugify(instance)
    return f'projects/{ad}/{filename}'


def proje_ust_path(instance,filename):
    ad=slugify(instance.proje)
    return f'projects/{ad}/{filename}'



class ProjeAçıklama(models.Model):
    tanim = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Açıklama"
    
class Proje(models.Model):
    id = models.AutoField(primary_key=True, unique=True)  # Auto-incrementing, unique id field
    ad = models.CharField(max_length=300, unique=False,null=False,default="Proje Adı")
    aciklama = RichTextField(blank=True, null=True)
    baslik= models.CharField(max_length=300, unique=False,blank=True)
    ozet= RichTextField(max_length=1000, unique=False,null=True)
    kategori=models.ForeignKey(Hizmet,null=True,on_delete=models.DO_NOTHING)
    proje_tarihi = models.DateTimeField(blank=True,null=True)
    kapak_resmi=models.ImageField(upload_to=proje_directory_path,default='projects/template.jpg',null=True,blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.ad
    def save(self, *args, **kwargs):
        if not self.pk:  # Yeni bir proje oluşturulurken
            self.order = Proje.objects.count() + 1
        if self.ad:
            self.baslik = slugify(self.ad)
        super().save(*args, **kwargs)
    class Meta:
        ordering = ['-order']  # ID'ye göre sıralama
class ProjeResim(models.Model):
    proje = models.ForeignKey(Proje, related_name='resimler', on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to=proje_ust_path,null=True)

    def __str__(self):
        return self.image.url
    
    def rotate_right(self):
        if self.image:
            # Resmi aç
            pil_image = PILImage.open(self.image.path)
            # 90 derece sağa döndür
            rotated_image = pil_image.rotate(-90, expand=True)
            # Döndürülmüş resmi kaydet
            rotated_image.save(self.image.path)
    