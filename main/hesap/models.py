from django.db import models

class Hesap(models.Model):
    ad=models.CharField(max_length=200, unique=True,null=False)
    baglanti=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
         return self.ad
    
class Telefon(models.Model):
    ad=models.CharField(max_length=20, unique=True,null=False)

    def __str__(self):
         return self.ad
class Mail(models.Model):
    ad=models.CharField(max_length=50, unique=True,null=False)
    
    def __str__(self):
         return self.ad
    
class Adres(models.Model):
    ad=models.TextField(max_length=300)
  
    def __str__(self):
         return self.ad