import factory
from djangocms_alias.models import Alias, AliasContent, Category

from testapp.models import Blog


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.Faker("sentence", nb_words=4)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category


class AliasContentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = AliasContent


class AliasFactory(factory.django.DjangoModelFactory):

    category = factory.SubFactory(CategoryFactory)

    static_code = factory.Faker("word")

    log = factory.RelatedFactory(
        AliasContentFactory,
        factory_related_name="alias",
    )

    class Meta:
        model = Alias
