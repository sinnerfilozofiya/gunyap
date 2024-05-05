from django.db import models

class Hesap(models.Model):
    ad=models.CharField(max_length=200, unique=True,null=False)
    baglanti=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
         return self.ad
    