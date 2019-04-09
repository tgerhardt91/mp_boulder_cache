from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import AreaCoordinate


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    areas = AreaCoordinate.objects.all()

    return render(request, "db.html", {"greetings": greetings, "areas": areas})


def manage(request):

    message = 'No selection made'

    if request.method == 'POST':
        area_selection = request.POST['area_selection']
        message = area_selection.name + ' selected'

    areas = AreaCoordinate.objects.all()

    return render(request, 'manage.html', {'message': message, 'areas': areas})



