from django.db import models

from apps.users.models import CustomUser


class StudentSponsor(models.Model):
    student = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE,related_name='student',null=True)
    sponsor = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE,related_name='sponsor',null=True)
    amount = balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
