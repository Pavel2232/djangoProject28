from rest_framework import serializers

from categories.models import Categorie


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = '__all__'

