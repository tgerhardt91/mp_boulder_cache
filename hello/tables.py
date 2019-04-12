
from .models import Problem
import django_tables2 as tables


class ProblemTable(tables.Table):
    class Meta:
        model = Problem
