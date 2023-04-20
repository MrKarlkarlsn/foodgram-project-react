from django_filters import rest_framework
from users.models import CustomUsers

from recipe.models import Ingredient, Recipe, Tag


class FilterIngredient(rest_framework.FilterSet):
    name = rest_framework.CharFilter(
        field_name='name',
        lookup_expr='istartswith'
    )

    class Meta:
        model = Ingredient
        fields = ('name', 'measurement_unit')


class FilterRecipe(rest_framework.FilterSet):
    tags = rest_framework.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
    )
    author = rest_framework.ModelChoiceFilter(
        queryset=CustomUsers.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author')
