from decimal import Decimal
from rest_framework.settings import api_settings

from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager

from apps.general.validation_phone import check_uzb_number



class CustomUserManager(UserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given phone number and password.
        """
        phone_number = check_uzb_number(phone_number)
        if not phone_number:
            raise ValueError("Invalid phone number")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractUser):
    class RoleChoices(models.TextChoices):
        STUDENT = 'student', 'Student'
        SPONSOR = 'sponsor', 'Sponsor'
        ADMIN = 'admin', 'Admin'

    class DegreeChoices(models.TextChoices):
        BACHELOR = 'bachelor', 'Bachelor'
        MAGISTR = 'magis', 'Magistr'

    class LegalType(models.TextChoices):
        personal = 'personal', 'Personal'
        legal = 'legal' 'Legal'
    username = None
    phone_number = models.CharField(max_length=13, validators=[check_uzb_number],unique=True)
    user_image = models.ImageField(upload_to='user_images/%Y/%m/%d', blank=True, null=True)
    user_type = models.CharField(
        max_length=100,
        choices=LegalType.choices,
        default=LegalType.personal,
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=100,
        choices=RoleChoices.choices,
        default=RoleChoices.STUDENT,
    )
    balance = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
    )
    available = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
    )
    university = models.ForeignKey(
        "general.University",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    degree = models.CharField(
        max_length=50,
        choices=DegreeChoices.choices,
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def clean(self):
        if self.role == self.RoleChoices.STUDENT and not self.university:
            raise ValidationError({'university':'The University area for the Student must be filled'})

    def __str__(self):
        return f"{self.phone_number} - {self.first_name} {self.last_name}"

UserModel = CustomUser