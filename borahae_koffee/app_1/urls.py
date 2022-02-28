# ~ borahae_koffee/app_1/urls.py
from django.urls import path, include
from app_1 import views
urlpatterns = [
    path('', views.sample_view, name='sample_view'),
]