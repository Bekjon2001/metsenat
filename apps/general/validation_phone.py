import re
from django.core.exceptions import ValidationError

def check_uzb_number(value):
    """Telefon raqami validatsiyasi"""
    if not re.match(r"^\+998\d{9}$", value):
        raise ValidationError("Invalid phone number")
    return value


