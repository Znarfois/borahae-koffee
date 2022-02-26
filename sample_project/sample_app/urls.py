# ~ sample_project/sample_app/urls.py
from django.urls import path, include
from sample_app import views
urlpatterns = [
    path('', views.sample_view, name='sample_view'),
]