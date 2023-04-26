from django_filters.rest_framework import FilterSet, filters
from recipe.models import Ingredient, Recipe

from users.models import CustomUsers


class FilterIngredient(FilterSet):
    name = filters.CharFilter(
        field_name='name', lookup_expr='icontains'
    )

    class Meta:
        model = Ingredient
        fields = ['name']


class FiltersRecipe(FilterSet):
    tags = filters.CharFilter(method='tags_filter')
    author = filters.ModelChoiceFilter(queryset=CustomUsers.objects.all())
    is_favorited = filters.BooleanFilter(method='favorited_filter')
    is_in_shopping_cart = filters.BooleanFilter(method='shop_filter')

    def shop_filter(self, queryset, name, value):
        if self.request.user.is_authenticated and value:
            return queryset.filter(shoppings=self.request.user)
        return queryset

    def favorited_filter(self, queryset, name, value):
        if self.request.user.is_authenticated and value:
            return queryset.filter(favorites=self.request.user)
        return queryset

    def tags_filter(self, queryset, name, value):
        filter_data = queryset.filter(tags__slug=value).exists()
        if filter_data:
            return filter_data
        return queryset

    class Meta:
        model = Recipe
        fields = [
            'author',
            'tags',
            'is_in_shopping_cart',
            'is_favorited'
        ]
