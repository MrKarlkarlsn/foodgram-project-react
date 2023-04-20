import django_filters

from users.models import CustomUsers

from recipe.models import Ingredient, Recipe, Tag


class FilterIngredient(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='istartswith'
    )

    class Meta:
        model = Ingredient
        fields = ('name', 'measurement_unit')


class FilterRecipe(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
    )
    author = django_filters.ModelChoiceFilter(
        queryset=CustomUsers.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author')
