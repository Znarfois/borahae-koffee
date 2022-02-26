# ~ sample_project/sample_project/urls.py
from django.contrib import admin
from django.urls import path, include
import sample_app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample_app/', include('sample_app.urls'))
]