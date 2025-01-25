from django.conf import settings
from django.db import models

from apps.general.models import PaymentMethod,BaseModel
from apps.general.validation_phone import check_uzb_number

class Appeal(BaseModel):
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='appeals')
    phone_number = models.CharField(max_length=13,validators=[check_uzb_number] )
    amount = models.DecimalField(decimal_places=2, max_digits=50)
    is_verified = models.BooleanField(default=False)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.sponsor_id}'
