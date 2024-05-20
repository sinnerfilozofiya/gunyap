from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxLengthValidator



def service_directory_path(instance,filename):
    return f'hizmetler/{filename}'


class HizmetAçıklama(models.Model):
    tanim = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Açıklama"
    
   

class Hizmet(models.Model):
    ad = models.CharField(max_length=200, unique=True,null=False)
    tanim = models.TextField(blank=True, null=True)
    baslik= models.CharField(max_length=300, unique=False,blank=True)
    image = models.ImageField(upload_to=service_directory_path,default="hizmetler/services.jpg")
    ozet= models.TextField(
        blank=True,
        null=True,
        default='Özet',
        validators=[MaxLengthValidator(500)]
    )
    
    def __str__(self):
        return self.ad
    
    def save(self, *args, **kwargs):
        if self.ad:
            self.baslik = slugify(self.ad)
        super().save(*args, **kwargs)