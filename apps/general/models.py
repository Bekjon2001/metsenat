import uuid
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    """
    Barcha odellar uchun assosiy Base model
    """
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    created_by=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='%(class)s_created_by'

    )


    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.celen()
        super().save(*args, **kwargs)

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
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name