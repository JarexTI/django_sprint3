from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PublishedAndCreatedAt(models.Model):
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(PublishedAndCreatedAt):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Mate:
        abstract = True


class Location(PublishedAndCreatedAt):
    name = models.CharField(max_length=256)

    class Mate:
        abstract = True


class Post(PublishedAndCreatedAt):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    class Mate:
        abstract = True
