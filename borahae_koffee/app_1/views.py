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
    return render(request, 'app_1/MyEvents.html')

def create_event(request):
    return render(request, 'app_1/create-event-flow-1.html')

def create_reservation(request):
    return render(request, 'app_1/createrev.html')

def create_feedback(request):
    return render(request, 'app_1/feedback system (1).html')

def dashboard(request):
    return render(request, 'app_1/dashboard.html')
