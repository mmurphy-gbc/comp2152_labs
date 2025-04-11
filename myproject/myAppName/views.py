# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Goodbye, world! This is your first Django view.")
