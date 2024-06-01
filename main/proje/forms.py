from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _



from .models import Proje,ProjeResim

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class FileFieldForm(forms.ModelForm):
    class Meta:
        model = Proje
        fields = (
            "ad",
            "aciklama",
            "kategori",
            "proje_tarihi",
            "kapak_resmi",
            "order",
            
        )
    photos = MultipleFileField()
    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, proje):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            photo = ProjeResim(proje=proje, image=upload)
            photo.save()

   
