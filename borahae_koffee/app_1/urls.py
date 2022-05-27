from django.urls import path, include
from app_1 import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create_event', views.create_event, name='create_event'),
    path('create_reservation', views.create_reservation, name='create_reservation'),
    path('create_feedback', views.create_feedback, name='create_feedback'),
    path('dashboard', views.dashboard, name='dashboard')
]