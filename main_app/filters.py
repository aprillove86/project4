import django_filters
from django_filters import DateFilter
from .models import Memo 

class MemoFilter(django_filters.FilterSet):

    start_date = DateFilter(label='Between', field_name='date', lookup_expr='gte')
    end_date = DateFilter(label='And', field_name='date', lookup_expr='lte')

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending'),
    )

    class Meta:
        model = Memo
        fields = {
            'tag_desc': ['icontains'],
        }
