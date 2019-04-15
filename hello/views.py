
from django.shortcuts import render
from django_tables2 import RequestConfig
from lib import problem_cache
import sys
import traceback

from .models import Greeting
from .models import AreaCoordinate
from .models import Problem
from .models import ProblemProcessor
from .tables import ProblemTable
from .filters import ProblemFilter


# Create your views here.
def index(request):
    areas = AreaCoordinate.objects.all()

    try:
        if request.method == 'POST':
            area_selection_id = request.POST['area_selection']
            problems = ProblemProcessor.get_by_area_id(area_selection_id)
        else:
            problems = Problem.objects.all()
    except:
        sys.stderr.write(traceback.format_exc())

    table = ProblemTable(problems)
    RequestConfig(request).configure(table)

    return render(request, "index.html", {"areas": areas}, {"table": table})


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
            sys.stderr.write(traceback.format_exc())

    areas = AreaCoordinate.objects.all()
    problems = Problem.objects.all()

    problem_filter = ProblemFilter(request.GET, queryset=problems)

    table = ProblemTable(problem_filter.qs)

    RequestConfig(request).configure(table)

    return render(request, 'managecache.html', {'message': message, 'areas': areas,
                                                'table': table, 'filter': problem_filter})





