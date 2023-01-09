import  factory

from ads.models import Ad, Compilation
from categories.models import Categorie
from user.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categorie

    slug = "Стихии123"
class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'test'
    password = 'test'
class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test"
    price = 10
    is_published = True
    # category = factory.SubFactory(CategoryFactory)


class CompilationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Compilation

    name = "test"