from django.urls import path, include
from app_1 import views
urlpatterns = [
    path('', views.sample_view, name='sample_view'),
    path('new_event', views.create_event, name="create_event"),
    path('create_reservation', views.create_reservation, name='create_reservation'),
    path('my_events', views.my_events, name='my_events')
]