from typing import Union
from blog.models import Post, Category, Location

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    template: str = 'blog/index.html'
    posts = Post.objects.filter(is_published=True)
    context = {'post': posts}
    return render(request, template, context)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    template: str = 'blog/detail.html'
    if pk not in POSTS_BY_ID:
        raise Http404('Ошибка 404')
    context: dict[str, POST] = {'post': POSTS_BY_ID[pk]}
    return render(request, template, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    template: str = 'blog/category.html'
    context: dict[str, str] = {'category_slug': category_slug}
    return render(request, template, context)
