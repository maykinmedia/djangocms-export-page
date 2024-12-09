from django.db import models
from django.urls import NoReverseMatch, reverse

from autoslug import AutoSlugField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = AutoSlugField(populate_from="title", editable=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
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
