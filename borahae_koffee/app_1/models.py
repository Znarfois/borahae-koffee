from django.db import models
from django.utils import timezone

# Create your models here.

class Accounts(models.Model):
    username = models.CharField(max_length=255,
    primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    PhoneNumber = models.PositiveSmallIntegerField()
    EMail = models.CharField(max_length=255)


