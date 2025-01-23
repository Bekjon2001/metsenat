from django.db import models

class RoleChoices(models.TextChoices):
    STUDENT = 'student', 'Student'
    TEACHER = 'teacher', 'Teacher'
    ADMIN = 'admin', 'Admin'

class DegreeChoices(models.TextChoices):
    BAKALAVR = 'bakalavr', 'Bakalavr'
    MAGISTR = 'magis', 'Magistr'