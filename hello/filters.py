from .models import Problem
import django_filters


class ProblemFilter(django_filters.FilterSet):
    class Meta:
        model = Problem
        fields = ['name']
