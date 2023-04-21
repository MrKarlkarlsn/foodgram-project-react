from django.db.models import Sum
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from users.models import CustomUsers

from recipe.models import Recipe, IngredientInRecipe
from recipe.serializer import RecipeSerializer, UserLikeRecipeSerializer
from recipe.permissions import IsAuthorOrAdmin
from recipe.generate_pdf import generate_pdf

from api.pagination import UserPagination


class RecipeViewset(ModelViewSet):
    """
    Эндпоинт ./recipes/
    """
    queryset = Recipe.objects.select_related('author').all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = UserPagination
    permission_classes = [IsAuthorOrAdmin,
                          IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(author=user)

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance,
                                         data=request.data,
                                         partial=True)
        serializer.is_valid()
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['POST', 'DELETE'],
        url_path=r'(?P<id>[\d]+)/favorite',
        url_name='favorite',
        pagination_class=None,
        permission_classes=[IsAuthenticated])
    def favorites(self, request, **kwargs):
        """Добавление и удаление рецепта в избранное"""
        recipe = get_object_or_404(Recipe, id=kwargs['id'])
        user = get_object_or_404(CustomUsers, id=request.user.id)
        recipe_like = CustomUsers.objects.filter(
            username=request.user.id,
            favorite_recipes=recipe,
        ).exists()

        if request.method == 'POST' and not recipe_like:
            user.favorite_recipes.add(recipe)
            serializer = UserLikeRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if request.method == 'DELETE' and recipe:
            user.favorite_recipes.remove(recipe)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'errors': 'Ошибка'},
            status.HTTP_400_BAD_REQUEST
        )

    @action(
        detail=False,
        methods=['POST', 'DELETE'],
        url_path=r'(?P<id>[\d]+)/shopping_cart',
        url_name='shopping_cart',
        pagination_class=None,
        permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, **kwargs):
        """Добавление и удаления рецепта из списка покупок"""
        recipe = get_object_or_404(Recipe, id=kwargs['id'])
        user = get_object_or_404(CustomUsers, id=request.user.id)
        queryset = CustomUsers.objects.filter(
            id=request.user.id,
            shopping_recipes=recipe
        ).exists()

        if request.method == 'POST' and not queryset:
            user.shopping_recipes.add(recipe)
            return Response(status=status.HTTP_201_CREATED)
        if request.method == 'DELETE' and queryset:
            user.shopping_recipes.remove(recipe)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'],
            detail=False,
            url_path='download_shopping_cart',
            url_name='cart',)
    def download_shopping_cart(self, request):
        """Скачавание PDF файла со списком покупок"""
        user = request.user
        qweryset = IngredientInRecipe.objects.filter(recipe__shoppings=user)
        qweryset_sort = qweryset.values('ingredient__name',
                                        'ingredient__measurement_unit',
                                        ).annotate(
            quantity=Sum('quantity')).order_by()
        return generate_pdf(qweryset_sort)
