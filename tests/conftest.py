from pytest_factoryboy import register

from tests.factories import AdFactory, AuthorFactory, CategoryFactory, CompilationFactory

pytest_plugins = "tests.fixtures"

register(AdFactory)
register(AuthorFactory)
register(CategoryFactory)
register(CompilationFactory)