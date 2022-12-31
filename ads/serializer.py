from rest_framework import serializers
from ads.models import Ad
from categories.models import Categorie


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="first_name")

    category = serializers.CharField(max_length=100)

    class Meta:
        model = Ad
        fields = ["name","author","category","price","description","is_published","image"]

class AdRetrieveSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="first_name")

    category = serializers.CharField(max_length=100)

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Categorie.objects.all(),
        slug_field = "name"
    )

    image = serializers.CharField(max_length=200)

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self,raise_exception=False):
        self._category = self.initial_data.pop("category")
        return  super().is_valid(raise_exception=raise_exception)


    def create(self, validated_data):
        ads = Ad.objects.create(**validated_data)

        categ_obj,_ = Categorie.objects.get_or_create(name=self._category)

        ads.category = categ_obj
        ads.save()

        return ads


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="first_name")

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Categorie.objects.all(),
        slug_field = "name"
    )

    image = serializers.CharField(max_length=200)
    class Meta:
        model = Ad
        fields = ["id","name","author","category","price","description","is_published","image"]

    def is_valid(self,raise_exception=False):
        self._category = self.initial_data.pop("category")
        return  super().is_valid(raise_exception=raise_exception)


    def save(self, **kwargs):
        ads = super().save()

        categ_obj,_ = Categorie.objects.get_or_create(name=self._category)

        ads.category = categ_obj
        ads.save()

        return ads


class AdDestroyserializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]