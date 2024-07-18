from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import (CASCADE, SET_NULL, BooleanField, CharField,
                              DateTimeField, ForeignKey, SlugField, TextField)

User = get_user_model()


class PublishedAndCreatedAt(models.Model):
    is_published: BooleanField = BooleanField(default=True)
    created_at: DateTimeField = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(PublishedAndCreatedAt):
    title: CharField = CharField(max_length=256)
    description: TextField = TextField()
    slug: SlugField = SlugField(unique=True)

    class Mate:
        abstract = True


class Location(PublishedAndCreatedAt):
    name: CharField = CharField(max_length=256)

    class Mate:
        abstract = True


class Post(PublishedAndCreatedAt):
    title: CharField = CharField(max_length=256)
    text: TextField = TextField()
    pub_date: DateTimeField = DateTimeField()
    author: ForeignKey = ForeignKey(
        User,
        on_delete=CASCADE
    )
    location: ForeignKey = ForeignKey(
        Location,
        on_delete=SET_NULL,
        blank=True,
        null=True)
    category: ForeignKey = ForeignKey(
        Category,
        on_delete=SET_NULL,
        null=True
    )

    class Mate:
        abstract = True
