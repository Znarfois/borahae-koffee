from django.contrib import admin

# Register your models here.
from .models import Accounts
admin.site.register(Accounts)

from .models import Event
admin.site.register(Event)

from .models import Reservation
admin.site.register(Reservation)