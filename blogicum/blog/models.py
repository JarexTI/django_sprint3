from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import (CASCADE, SET_NULL, BooleanField, CharField,
                              DateTimeField, ForeignKey, SlugField, TextField)

User = get_user_model()


class PublishedAndCreatedAt(models.Model):
    is_published: BooleanField = BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at: DateTimeField = DateTimeField(auto_now_add=True,
                                              verbose_name='Добавлено')

    class Meta:
        abstract = True


class Category(PublishedAndCreatedAt):
    title: CharField = CharField(max_length=256, verbose_name='Заголовок')
    description: TextField = TextField(verbose_name='Описание')
    slug: SlugField = SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.')
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(PublishedAndCreatedAt):
    name: CharField = CharField(max_length=256, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(PublishedAndCreatedAt):
    title: CharField = CharField(max_length=256, verbose_name='Заголовок')
    text: TextField = TextField(verbose_name='Текст')
    pub_date: DateTimeField = DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время в будущем '
                   '— можно делать отложенные публикации.')
    )
    author: ForeignKey = ForeignKey(
        User,
        on_delete=CASCADE,
        verbose_name='Автор публикации'
    )
    location: ForeignKey = ForeignKey(
        Location,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        verbose_name='Местоположение'
    )
    category: ForeignKey = ForeignKey(
        Category,
        on_delete=SET_NULL,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
