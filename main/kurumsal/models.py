from django.db import models


def about_directory_path(instance,filename):
    return f'hakkimizda/{filename}'

def misyonumuz_directory_path(instance,filename):
    return f'misyonumuz/{filename}'
def vizyonumuz_directory_path(instance,filename):
    return f'vizyonumuz/{filename}'

class Madde(models.Model):
    ad=models.CharField(max_length=200, unique=True,null=False)
    aciklama=models.CharField(max_length=200,null=False,default="Açıklama")
    def __str__(self):
         return self.ad

class BizKimiz(models.Model):
    tanim=models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=about_directory_path,default="hakkimizda/about.jpg")
    def __str__(self):
         return f"Biz Kimiz"
    
class Misyonumuz(models.Model):
    tanim=models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=misyonumuz_directory_path,default="misyonumuz/mission.jpg")
    madde=models.ManyToManyField(Madde, blank=True)

    def __str__(self):
         return f"Misyonumuz"

class Vizyonumuz(models.Model):
    tanim=models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=vizyonumuz_directory_path,default="vizyonumuz/vision.jpg")
    madde=models.ManyToManyField(Madde, blank=True)
    def __str__(self):
         return f"Vizyonumuz"



def document_directory_path(instance,filename):
    return f'documents/{filename}'


class Belge(models.Model):
    ad=models.CharField(max_length=200, unique=True,null=False)
    belge = models.FileField(upload_to=document_directory_path,default="documents/isguvenligi.pdf")
    def __str__(self):
         return self.ad

Madde._meta.verbose_name_plural = "Maddeler"
BizKimiz._meta.verbose_name_plural = "Biz Kimiz"
Misyonumuz._meta.verbose_name_plural = "Misyonumuz"
Vizyonumuz._meta.verbose_name_plural = "Vizyonumuz"
Belge._meta.verbose_name_plural = "Belgeler"
