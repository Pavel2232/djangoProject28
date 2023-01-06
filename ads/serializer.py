
from rest_framework import serializers

from ads.models import Ad, Compilation
from categories.models import Categorie


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="username")

    category = serializers.CharField(max_length=100)

    class Meta:
        model = Ad
        fields = ["name","author","category","price","description","is_published","image"]

class AdRetrieveSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="username")

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



class CompilationSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(read_only=True,
                                          slug_field="username")
    ads = serializers.SlugRelatedField(read_only=True,
                                       slug_field="name",
                                       many=True)

    class Meta:
        model = Compilation
        fields = "__all__"

class CompilationRetrieveSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(read_only=True,
                                          slug_field="username")
    ads = AdRetrieveSerializer(many=True)

    class Meta:
        model = Compilation
        fields = "__all__"

class CompilationCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    ads = serializers.SlugRelatedField(required= False,
                                       queryset=Ad.objects.all(),
                                       slug_field="name",
                                       many=True)

    class Meta:
        model = Compilation
        fields = '__all__'
    def is_valid(self, raise_exception=False):
        self._author = self.context['request'].user
        self._ads = self.initial_data.pop("ads")
        return super().is_valid(raise_exception=raise_exception)


    # def save(self):
    #     author = CurrentUserDefault()

    def create(self, validated_data):
        compilation = Compilation.objects.create(**validated_data)

        for ad in self._ads:
            ads_obj, _ = Ad.objects.get_or_create(id= ad)
            compilation.ads.add(ads_obj)


        compilation.save()

        return compilation

class CompilationUpdateSerializer(serializers.ModelSerializer):


    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="username"
                                                     "")
    name = serializers.CharField(max_length=100)

    ads = serializers.SlugRelatedField(
        required=False,
        queryset=Ad.objects.all(),
        slug_field="name",
        many=True
    )


    def is_valid(self, raise_exception=False):
        self._ads = self.initial_data.pop("ads")
        super().is_valid(raise_exception=raise_exception)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        ads = []
        for ad in self._ads:
            obj, _= Ad.objects.get_or_create(id= ad)
            ads.append(obj)
        instance.ads.set(ads)
        instance.save()
        return instance

    class Meta:
        model = Compilation
        fields = '__all__'


class CompilationDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Compilation
        fields = ["id"]