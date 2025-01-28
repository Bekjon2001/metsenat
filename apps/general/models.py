from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator

from apps.utils.models.base_model import BaseModel


class University(BaseModel):
    name = models.CharField(max_length=100)
    contract_amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('1'))]
    )

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50, default="Active")

    def __str__(self):
        return self.name
