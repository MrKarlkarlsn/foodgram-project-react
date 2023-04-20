from django_filters import CharFilter, FilterSet

from recipe.models import Ingredient


class FilterIngredient(FilterSet):
    name = CharFilter(
        field_name='name', lookup_expr='startswith'
    )

    class Meta:
        model = Ingredient
        fields = ['name']
