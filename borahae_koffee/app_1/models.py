from django.db import models
from django.utils import timezone

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=255,
    primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    PhoneNumber = models.PositiveSmallIntegerField()
    Email = models.CharField(max_length=255)

    objects = models.Manager()

class Event(models.Model):
    EventID = models.PositiveSmallIntegerField(primary_key=True)
    EventName = models.CharField(max_length=255)
    EventStartDate = models.DateField()
    EventEndDate = models.DateField()
    EventDescription = models.TextField(max_length=65535)
    EventAvailableSlots = models.PositiveSmallIntegerField()
    EventMaximumCapacity = models.PositiveSmallIntegerField()
    EventStartTime = models.TimeField()
    EventEndTime = models.TimeField()
    EventStatus = models.TextField(max_length=255)

    objects = models.Manager()
    #Status with DtypeENUM to be made pa as a subclass :)

class Reservation(models.Model):
    ReservationNum = models.PositiveSmallIntegerField(
        primary_key=True)
    ReservationDate = models.DateField()
    ReservationTimeSlot = models.TimeField()
    ReservationNumberOfPeople = models.PositiveSmallIntegerField()
    ReservationConfirmationStatus = models.BooleanField()
    ReservationAttendance = models.BooleanField()
    EventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    username = models.ForeignKey(Account, on_delete=models.CASCADE)

    objects = models.Manager()


#Class Reservation
#Class Reservation Additional Detail
#Class Feedback
#Class Feedback Question Answer





    
