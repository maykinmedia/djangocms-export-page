from django.db import models
from django.urls import NoReverseMatch, reverse
from django.utils.functional import cached_property

from cms.models.fields import PlaceholderRelationField
from cms.utils.placeholder import get_placeholder_from_slot

from autoslug import AutoSlugField


# Create your models here.
class Blog(models.Model):

    _export_page = {
        "sections": [
            {"name": "Meta", "fields": ["title", "slug", "date_posted"]},
            {"name": "Body", "fields": ["content"]},
        ],
    }

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    placeholders = PlaceholderRelationField()

    @cached_property
    def content(self):
        return get_placeholder_from_slot(self.placeholders, "blog_content")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            return reverse(
                "blog:detail",
                kwargs={
                    "slug": self.slug,
                },
            )
        except NoReverseMatch:
            pass
        return ""

    def get_title(self):
        return self.title

    @property
    def template(self):
        return "blog.html"
