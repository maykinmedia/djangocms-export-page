import factory

from testapp.models import Blog


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.Faker("sentence", nb_words=4)
    content = factory.Faker("text")
