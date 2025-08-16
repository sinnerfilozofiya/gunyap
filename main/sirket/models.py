from django.db import models
from django.contrib.auth.models import User

class Sirket(models.Model):
    ad = models.CharField(max_length=200, unique=True, null=False)
    calisanlar = models.ManyToManyField(User, through='SirketCalisan', related_name='sirket')

    def __str__(self):
        return self.ad

class SirketCalisan(models.Model):
    sirket = models.ForeignKey(Sirket, on_delete=models.CASCADE)
    calisan = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # Ensure that each user can only be associated with one company
        constraints = [
            models.UniqueConstraint(fields=['sirket', 'calisan'], name='uniq_sirket_calisan')
        ]

    def __str__(self):
        return f"{self.calisan.username} in {self.sirket.ad}"
