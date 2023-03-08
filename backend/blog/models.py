from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django_extensions.db.fields import AutoSlugField
# Create your models here.


def rewrite_slug(content):
    return content.replace(' ', '_').lower()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.URLField(max_length=1000, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title', slugify_function=rewrite_slug)

    def __str__(self):
        return self.title
