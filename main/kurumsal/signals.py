from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Belge, BelgeOge

@receiver(pre_save, sender=Belge)
def create_belgeoge(sender, instance, **kwargs):
    print("selam")  # Bu satırı kontrol et
    print(f"kwargs: {kwargs}")  # kwargs içeriğini yazdır
    belgeoge = BelgeOge(belge=instance)
    
    # kwargs içindeki dosyayı kontrol et
    if 'dosya' in kwargs:
        dosya = kwargs.get('dosya')
        print(f"dosya: {dosya}")  # Dosyanın burada gelip gelmediğini kontrol et
        if dosya:
            belgeoge.dosya = dosya
            belgeoge.save()
