from rest_framework.viewsets import ModelViewSet

from categories.models import Categorie
from categories.serializer import CategoryListSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategoryListSerializer
