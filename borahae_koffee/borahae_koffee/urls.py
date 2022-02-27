# ~ sample_project/sample_project/urls.py
from django.contrib import admin
from django.urls import path, include
import app_1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_1/', include('app_1.urls'))
]