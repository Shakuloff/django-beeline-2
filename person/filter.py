import django_filters
# from django_filters import RangeFilter, RangeField
from .models import Person, Country, City
from django.db.models.constants import LOOKUP_SEP
from django.template.defaulttags import register


class detail_filter(django_filters.FilterSet):
    # country_filter = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    # salary__gt = django_filters.NumberFilter(field_name='Salary', lookup_expr='lt')
    # Salary = django_filters.NumberFilter()
    print(django_filters.filterset)
    # Salary__gt = django_filters.NumberFilter(field_name='Salary', lookup_expr='__gte')
    Salary = django_filters.NumberFilter(field_name='Salary', lookup_expr='gt')
    # price__gt = django_filters.NumberFilter(field_name='Salary', lookup_expr='gt')
    # Salary = RangeFilter()

    class Meta:
        model = Person
        fields = {
            'Gender',
            'Job',
            # 'Salary',
            'Countries',
            'Cities',
        }


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)