from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from django.core.files.base import ContentFile
from django.forms import ValidationError
import fitz 

def about_directory_path(instance,filename):
    return f'hakkimizda/{filename}'

def misyonumuz_directory_path(instance,filename):
    return f'misyonumuz/{filename}'
def vizyonumuz_directory_path(instance,filename):
    return f'vizyonumuz/{filename}'
def cover_directory_path(instance,filename):
    belge_adi=instance.ad
    return f'kapak/{belge_adi}/{filename}'

def document_directory_path(instance,filename):
    return f'documents/{instance.belge.pk}/{filename}'
def document_image_directory_path(instance,filename):
    return f'documents/image/{instance.belge.pk}/{filename}'

class Madde(models.Model):
    ad=models.CharField(max_length=200, unique=True,null=False)
    aciklama=RichTextField(max_length=200,null=False,default="Açıklama")
    def __str__(self):
         return self.ad

class BizKimiz(models.Model):
    tanim=RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to=about_directory_path,default="hakkimizda/about.jpg")
    e_katalog=models.FileField(upload_to=document_directory_path,null=True)
    def __str__(self):
         return f"Biz Kimiz"
    
class Misyonumuz(models.Model):
    tanim=RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to=misyonumuz_directory_path,default="misyonumuz/mission.jpg")
    madde=models.ManyToManyField(Madde, blank=True)

    def __str__(self):
         return f"Misyonumuz"

class Vizyonumuz(models.Model):
    tanim=RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to=vizyonumuz_directory_path,default="vizyonumuz/vision.jpg")
    madde=models.ManyToManyField(Madde, blank=True)
    def __str__(self):
         return f"Vizyonumuz"



class Belge(models.Model):
    ad = models.CharField(max_length=200, unique=False, null=False)
    kapak_resmi = models.ImageField(upload_to=cover_directory_path, default="kapak/taban.jpeg")
    
    def __str__(self):
        return self.ad



class BelgeOge(models.Model):
    belge = models.ForeignKey(Belge, related_name='belgeler', on_delete=models.SET_NULL,null=True)
    dosya = models.FileField(upload_to=document_directory_path,null=True)
    pdf_resim = models.ImageField(upload_to=document_image_directory_path, null=True, blank=True)
    
    def __str__(self):
        return self.dosya.url
    
    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        if self.dosya and self.dosya.name.endswith('.pdf'):
            # Convert PDF to Image
            pdf_image = self.convert_pdf_to_image(self.dosya.path)
            
            # Generate the filename for the image
            image_filename = f"{self.dosya.name.split('.')[0]}.png"
            
            # Save the image to the pdf_resim field
            image_path = document_image_directory_path(self, image_filename)
            image_file = ContentFile(pdf_image)
            self.pdf_resim.save(image_filename, image_file, save=False)

        # Call the parent class's save method
        super().save(*args, **kwargs)

    def convert_pdf_to_image(self, pdf_path):
        # Open the PDF with PyMuPDF (fitz)
        doc = fitz.open(pdf_path)

        # Get the first page and convert it to a pixmap (image)
        page = doc.load_page(0)  # Page numbering starts from 0
        pix = page.get_pixmap()

        # Convert the pixmap to a PNG image
        img_data = pix.tobytes("png")
        
        return img_data
Madde._meta.verbose_name_plural = "Maddeler"
BizKimiz._meta.verbose_name_plural = "Biz Kimiz"
Misyonumuz._meta.verbose_name_plural = "Misyonumuz"
Vizyonumuz._meta.verbose_name_plural = "Vizyonumuz"
Belge._meta.verbose_name_plural = "Belgeler"
