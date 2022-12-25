from rest_framework import serializers
from ads.models import Ad

class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
    read_only = True,
    slug_field = "name")

    category =serializers.SlugRelatedField(
    read_only = True,
    slug_field = "name")

   class Meta:
       model = Ad
       fields = ["__all__"]

       
