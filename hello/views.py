from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import AreaCoordinates


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    areas = AreaCoordinates.objects.all()

    return render(request, "db.html", {"greetings": greetings, "areas": areas})

