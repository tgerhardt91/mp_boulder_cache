from .models import Problem
import django_tables2 as tables


class ProblemTable(tables.Table):
    class Meta:
        model = Problem
        template_name = 'django_tables2/bootstrap.html'
        fields = ('name', 'grade', 'gmap_url', 'location', 'mp_url')

    # map = tables.TemplateColumn('<a href="{{record.gmap_url}}">map link</a>')
