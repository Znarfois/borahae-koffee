# ~ sample_project/sample_app/views.py
from django.http import HttpResponse
def sample_view(request):
    return HttpResponse("Hello, world!")