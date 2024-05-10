from django.db import models



def slider_directory_path(instance,filename):
    return f'slider/{filename}'

class Slogan(models.Model):
    tanim = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Açıklama"
    
class SlaytAçıklama(models.Model):
    tanim = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Açıklama"
    


class Slayt(models.Model):
    image = models.ImageField(upload_to=slider_directory_path,default="slider/idle.jpg")
    order = models.IntegerField(unique=True,blank=True,null=True)
    
    def __str__(self):
         return f"Slayt"
    
    def save(self, *args, **kwargs):
        if not self.order:
            # Eğer sıralama belirtilmemişse, sonraki benzersiz sıralama numarasını otomatik olarak atayın
            last_slide = Slayt.objects.order_by('-order').first()
            if last_slide:
                self.order = last_slide.order + 1
            else:
                self.order = 1
        super().save(*args, **kwargs)
    
