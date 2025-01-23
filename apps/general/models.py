from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100)
    contract_amount = models.DecimalField(max_digits=20, decimal_places=2)


class PuymetMetod(models.Model):
    name = models.CharField(max_length=100)
