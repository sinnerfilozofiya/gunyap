from django.db import models





class Mesaj(models.Model):
    gönderen=models.CharField(max_length=100,null=False)
    mail=models.EmailField(null=False)
    telefon=models.CharField(max_length=11,null=False, blank=False)
    tarih=models.DateTimeField(auto_now_add=True)
    konu=models.CharField(max_length=100,null=False)
    mesaj=models.TextField(blank=False, null=False)
  
    def __str__(self):
         return self.gönderen
    
