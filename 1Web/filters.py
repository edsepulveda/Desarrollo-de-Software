from django.db.models import fields
import django_filters
from django_filters import CharFilter


from .models import *


class ProductoFilter(django_filters.FilterSet):
    marca = CharFilter(field_name='marca', lookup_expr='icontains')
    class Meta:
        model = Producto
        fields = ['marca', 'tipo_categoria']

