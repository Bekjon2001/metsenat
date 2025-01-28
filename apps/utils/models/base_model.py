import uuid

from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    """
    Barcha odellar uchun assosiy Base model
    """
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+"

    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
