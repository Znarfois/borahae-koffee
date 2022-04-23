from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime
from django.http import HttpResponse

def sample_view(request):
    return HttpResponse("Hello, world!")

def create_event(request):
    return render(request, 'app_1/create-event-flow-1.html')

def create_reservation(request):
    return render(request, 'app_1/createrev.html')

def my_events(request):
    return render(request, 'app_1/MyEvents.html')
