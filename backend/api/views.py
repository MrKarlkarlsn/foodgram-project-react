from api.serializer import TagSerializer, IngredientsSerializer
from api.filters import FilterIngredient

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from recipe.models import Tag, Ingredient


class TagsViewsSet(ReadOnlyModelViewSet):
    """Получение тегов. Эндпоинт ./tags/<id>/"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class IngredientsViewsSet(ReadOnlyModelViewSet):
    """Получение тегов. Эндпоинт ./ingredients/<id>/"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [AllowAny]
    filterset_class = FilterIngredient
    pagination_class = None
