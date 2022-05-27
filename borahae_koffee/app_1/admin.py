from django.contrib import admin

# Register your models here.
from .models import Account
admin.site.register(Account)

from .models import Event
admin.site.register(Event)

from .models import Reservation
admin.site.register(Reservation)