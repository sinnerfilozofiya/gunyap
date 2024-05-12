from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ad Soyad')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=15, label='Telefon')
    subject = forms.CharField(max_length=100, label='Konu')
    message = forms.CharField(widget=forms.Textarea, label='Mesaj')
