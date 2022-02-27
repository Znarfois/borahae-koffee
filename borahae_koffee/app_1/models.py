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

class Event(models.Model):
    EventID = models.PositiveSmallIntegerField(primary_key=True)
    EventName = models.CharField(max_length=255)
    EventDate = models.DateField()
    EventDescription = models.TextField(max_length=65535)
    EventAvailableSlots = models.PositiveSmallIntegerField()
    EventMaximumCapacity = models.PositiveSmallIntegerField()
    EventTime = models.TimeField()
    #Status with DtypeENUM to be made pa as a subclass :)

#Class Reservation
#Class Reservation Additional Detail
#Class Feedback
#Class Feedback Question Answer





    
