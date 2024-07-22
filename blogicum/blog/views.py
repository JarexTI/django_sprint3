from datetime import date
from typing import Union

from blog.models import Category, Post
from .const import LIMIT_POSTS
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render


def index(request: HttpRequest) -> HttpResponse:
    template: str = 'blog/index.html'

    post_list: QuerySet[Post] = Post.objects.filter(
        pub_date__lte=date.today(),
        is_published=True,
        category__is_published=True
    )[:LIMIT_POSTS]

    context: dict[str, QuerySet[Post]] = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    template: str = 'blog/detail.html'
    post: Post = get_object_or_404(
        Post,
        pk=pk,
        pub_date__lte=date.today(),
        is_published=True,
        category__is_published=True
    )

    context: dict[str, Post] = {'post': post}
    return render(request, template, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    template: str = 'blog/category.html'
    post_list: list[Post] = get_list_or_404(
        Post,
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=date.today()
    )

    category: Category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    context: dict[str, Union[list[Post], Category]] = {
        'post_list': post_list,
        'category': category
    }
    return render(request, template, context)
