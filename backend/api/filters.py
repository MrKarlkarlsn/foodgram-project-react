from django_filters import CharFilter, FilterSet, filters

from recipe.models import Ingredient, Recipe

from users.models import CustomUsers


class FilterIngredient(FilterSet):
    name = CharFilter(
        field_name='name', lookup_expr='startswith'
    )

    class Meta:
        model = Ingredient
        fields = ['name']


class FoltersRecipe(FilterSet):
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    author = filters.ModelChoiceFilter(queryset=CustomUsers.objects.all())
    is_favorited = filters.BooleanFilter(method='favorites_filter')
    is_in_shopping_cart = filters.BooleanFilter(method='shop_filter')

    def shop_filter(self, queryset, name, value):
        if self.request.user.is_authenticated and value:
            return queryset.filter(shoppings=self.request.user)
        return queryset

    def favorites_filter(self, queryset, name, value):
        if self.request.user.is_authenticated and value:
            return queryset.filter(favorites=self.request.user)
        return queryset

    class Meta:
        model = Recipe
        fields = [
            'author',
            'tags'
        ]
