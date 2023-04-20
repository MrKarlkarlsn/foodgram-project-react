from api.serializer import TagSerializer, IngredientsSerializer
from api.filters import FilterIngredient

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from django_filters.rest_framework import DjangoFilterBackend

from recipe.models import Tag, Ingredient


class TagsViewsSet(ReadOnlyModelViewSet):
    """Получение тегов. Эндпоинт ./tags/<id>/"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class IngredientsViewsSet(ReadOnlyModelViewSet):
    """Получение тегов. Эндпоинт ./ingredients/<id>/"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilterIngredient
