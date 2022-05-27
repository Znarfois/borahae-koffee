from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime
from django.http import HttpResponse
# import pyrebase

# config = {
#     'apiKey': "AIzaSyAXgxhyHfYmcAtf8d7G7k8s2SKnM2sf-44",
#     'authDomain': "borahae-koffee.firebaseapp.com",
#     'projectId': "borahae-koffee",
#     'storageBucket': "borahae-koffee.appspot.com",
#     'messagingSenderId': "89657985195",
#     'appId': "1:89657985195:web:6d484438d84b7ccf5e8fee",
#     'measurementId': "G-CDGEGWREY1"
# }

# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database = firebase.database()

def index(request):
    events = Event.objects.all()
    return render(request, 'app_1/MyEvents.html', {"events":events})

def create_event(request):
    message = ""
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        name = request.POST.get('event_title')
        description = request.POST.get('event_description')
        start_date = request.POST.get('event_start_date')
        end_date = request.POST.get('event_end_date')
        start_time = request.POST.get('event_start_time')
        end_time = request.POST.get('event_end_time')
        participants = request.POST.get('participants')
        max_participants = request.POST.get('max_participants')
        status = request.POST.get('status')
        if Event.objects.filter(EventStartDate=start_date).exists():
            message="Date already taken. Please try again"
            return render(request, 'app_1/create-event-flow-1.html', {'message': message})
        if start_date > end_date:
            message="Start date must be before End date. Please try again"
            return render(request, 'app_1/create-event-flow-1.html', {'message': message})
        if int(max_participants) > 999:
            message="Invalid information. Please try again."
            return render(request, 'app_1/create-event-flow-1.html', {'message': message})
        Event.objects.create(EventID=event_id, EventName=name, EventDescription=description, EventAvailableSlots=participants, EventMaximumCapacity=max_participants, EventStartDate=start_date, EventEndDate=end_date, EventStartTime=start_time, EventEndTime=end_time, EventStatus=status)
        return redirect('create_reservation')
    return render(request, 'app_1/create-event-flow-1.html', {'message': message})

def update_event(request, event_id):
    success = ""
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        name = request.POST.get('event_title')
        description = request.POST.get('event_description')
        start_date = request.POST.get('event_start_date')
        end_date = request.POST.get('event_end_date')
        start_time = request.POST.get('event_start_time')
        end_time = request.POST.get('event_end_time')
        participants = request.POST.get('participants')
        max_participants = request.POST.get('max_participants')
        status = request.POST.get('status')
        Event.objects.filter(EventID=event_id).update(EventID=event_id, EventName=name, EventDescription=description, EventAvailableSlots=participants, EventMaximumCapacity=max_participants, EventStartDate=start_date, EventEndDate=end_date, EventStartTime=start_time, EventEndTime=end_time, EventStatus=status)
        success = "Event Updated!"
        events = Event.objects.all()
        return render(request, 'app_1/MyEvents.html', {"events":events, 'success':success})

    events = Event.objects.filter(EventID=event_id)
    return render(request, 'app_1/event_details.html', {'events': events})
    

def create_reservation(request):
    if request.method == 'POST':
        return redirect('create_feedback')
    return render(request, 'app_1/createrev.html')

def delete_event(request, event_id):
    success = ""
    Event.objects.filter(EventID=event_id).delete()
    success = "Event successfully delete!"
    events = Event.objects.all()
    return render(request, 'app_1/MyEvents.html', {"events":events, 'success':success})

def create_feedback(request):
    return render(request, 'app_1/feedback system (1).html')

def dashboard(request):
    return render(request, 'app_1/dashboard.html')