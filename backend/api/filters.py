from django_filters import rest_framework

from recipe.models import Ingredient, Recipe


class FilterRecipe(rest_framework.FilterSet):
    """
    """
    is_favorited = rest_framework.BooleanFilter(
        method='get_favorite',
        label='favorite',
    )
    tags = rest_framework.AllValuesMultipleFilter(
        field_name='tags__slug',
        label='tags',
    )
    is_in_shopping_cart = rest_framework.BooleanFilter(
        method='get_is_in_shopping_cart',
        label='shopping_cart',
    )

    class Meta:
        model = Recipe
        fields = (
            'tags',
            'author',
            'is_favorited',
            'is_in_shopping_cart',
        )

    def get_favorite(self, queryset, value):
        if value:
            return queryset.filter(in_favorite__user=self.request.user)
        return queryset.exclude(
            in_favorite__user=self.request.user
        )

    def get_is_in_shopping_cart(self,value):
        if value:
            return Recipe.objects.filter(
                shopping_recipe__user=self.request.user
            )


class FilterIngredient(rest_framework.filterset):
    name = rest_framework.CharFilter(
        field_name='name',
        lookup_expr='istartswith',
    )

    class Meta:
        model = Ingredient
        fields = ('name',)
