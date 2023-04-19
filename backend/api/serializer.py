from rest_framework import serializers

from recipe.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Получение тегов"""
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'color',
            'slug',
        )


class IngredientsSerializer(serializers.ModelSerializer):
    """Получение ингридиентов"""
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'measurement_unit',
        )
