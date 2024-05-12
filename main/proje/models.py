from django.db import models
from django.utils.text import slugify
from hizmet.models import Hizmet


def proje_directory_path(instance,filename):
    proje_adı = instance.baslik
    print(proje_adı)
    return f'projects/{proje_adı}/{filename}'

class ProjeAçıklama(models.Model):
    tanim = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Açıklama"
    
class Proje(models.Model):
    ad = models.CharField(max_length=200, unique=True,null=False,default="Proje Adı")
    aciklama = models.TextField(blank=True, null=True)
    baslik= models.CharField(max_length=300, unique=False,blank=True)
    ozet= models.CharField(max_length=1000, unique=True,null=True)
    kategori=models.ForeignKey(Hizmet,null=True,on_delete=models.DO_NOTHING)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)
    kapak_resmi=models.ImageField(upload_to=proje_directory_path,default='projects/template.jpg')

    def __str__(self):
        return self.ad
    def save(self, *args, **kwargs):
        if self.ad:
            self.baslik = slugify(self.ad)
        super().save(*args, **kwargs)

class ProjeResim(models.Model):
    proje = models.ForeignKey(Proje, related_name='resimler', on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to=proje_directory_path,null=True)


    def __str__(self):
        return self.image.url
    
    