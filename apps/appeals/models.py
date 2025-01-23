from django.db import models

from apps.general.models import PuymetMetod

class Appeal(models.Model):
    sponsor = models.ForeignKey('apps.Sponsor', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    is_verified = models.BooleanField(default=False)
    paymethod = models.ForeignKey(PuymetMetod, on_delete=models.CASCADE)
