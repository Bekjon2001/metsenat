from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from apps.general.validation_phone import check_uzb_number
from apps.general.roles import RoleChoices,DegreeChoices
from apps.general.models import University


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
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    user_type = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(
        max_length=10,
        choices=RoleChoices.choices,
    )
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    university = models.ForeignKey(
        University,
        on_delete=models.SET_NULL,
    )
    degree = models.CharField(
        max_length=50,
        choices=DegreeChoices.choices
    )


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.phone_number} - {self.first_name} {self.last_name}"
