
from django.shortcuts import render
from lib import problem_cache
import sys

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


def managecache(request):

    message = 'No selection made'

    if request.method == 'POST':
        area_selection_id = request.POST['area_selection']
        selected = AreaCoordinate.objects.get(id=int(area_selection_id))

        message = 'mountainproject data for ' + selected.name + ' cached'

        try:
            problem_cache.cache_problems_at_coordinates(selected.lat, selected.lon, area_selection_id)
        except Exception as e:
            message = 'caching data for ' + selected.name + ' failed, see error logs for details'
            sys.stderr.write('Error thrown while attempting to cache mp problem data, message: ' + str(e))

    areas = AreaCoordinate.objects.all()

    return render(request, 'managecache.html', {'message': message, 'areas': areas})





