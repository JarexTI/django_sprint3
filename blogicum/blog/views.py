from datetime import date
from typing import Union

from blog.models import Category, Post
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render


def index(request: HttpRequest) -> HttpResponse:
    template: str = 'blog/index.html'

    post_list: list[Post] = get_list_or_404(
        Post,
        pub_date__lte=date.today(),
        is_published=True,
        category__is_published=True
    )

    context: dict[str, list] = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    template: str = 'blog/detail.html'

    post: Post = get_object_or_404(Post, pk=pk)
    if (not post.is_published
        or not post.category.is_published
            or not post.pub_date.date() <= date.today()):
        raise Http404('Ошибка 404')

    context: dict[str, Post] = {'post': post}
    return render(request, template, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    template: str = 'blog/category.html'
    post_list: list[Post] = get_list_or_404(
        Post,
        is_published=True,
        pub_date__lte=date.today(),
        category__slug=category_slug
    )

    category: Category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        raise Http404('Ошибка 404')

    context: dict[str, Union[list[Post], Category]] = {
        'post_list': post_list,
        'category': category
    }
    return render(request, template, context)
