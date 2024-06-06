from django.db import models
from ckeditor.fields import RichTextField




def mesaj_directory_path(instance,filename):
    return f'kariyer/{filename}'

# Create your models here.
class KariyerAçıklama(models.Model):
    tanim = RichTextField(blank=True, null=True)
    def __str__(self):
        return f"Açıklama"
    
class KariyerGörsel(models.Model):
    tanim=models.CharField(max_length=50,null=True,default='Kariyer Görseli')
    image = models.ImageField(upload_to=mesaj_directory_path,default="kariyer/about.jpg")
    def __str__(self):
        return f"Görsel"