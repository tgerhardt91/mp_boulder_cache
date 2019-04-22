
from .models import Problem
import django_tables2 as tables


class ProblemTable(tables.Table):
    class Meta:
        model = Problem
        template_name = 'django_tables2/bootstrap.html'

    name = tables.Column()
    grade = tables.Column()
    map = tables.TemplateColumn('<a href="{{record.gmap_url}}">map link</a>')
    location = tables.Column()
    mp_url = tables.Column()
