from decimal import Decimal
from config import settings

from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


from apps.general.models import BaseModel
from apps.users.models import UserModel


class StudentSponsor(BaseModel):
    student = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student',
        null=True,
        limit_choices_to={'role': UserModel.RoleChoices.STUDENT},
    )
    sponsor = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sponsor',
        null=True,
        limit_choices_to={'available__gt': 0,'role': UserModel.RoleChoices.SPONSOR},
    )
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
    )
    is_verified = models.BooleanField()#?
    payment_method = models.ForeignKey('general.PaymentMethod', on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)


    def celen(self):
        if self.amount > self.sponsor.available:
            raise ValidationError({'amount':'The donation amount exceeds the sponsor\'s available funds.'})
        if self.amount > self.student.university.contract_amount - self.sponsor.balance:
            raise ValidationError({'amount':'the amount of charity exceeds the available funds of student contract.'})


    def __str__(self):
        return f"{self.sponsor_id} {self.student_id}"