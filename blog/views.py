from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Tag
from django.core.paginator import Paginator
from django.db.models import Q


# Контроллеры постов
def previous_next_url(page):
    if page.has_previous():
        previous_url = str(page.previous_page_number())
    else:
        previous_url = None
    if page.has_next():
        next_url = str(page.next_page_number())
    else:
        next_url = None

    return previous_url, next_url


class PostsList(View):
    """ Обрабатывает список постов """

    def get(self, request, page_number):
        search_query = request.GET.get('search', '')
        if search_query:
            posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        else:
            posts = Post.objects.all()
        
        paginator = Paginator(posts, 3)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()
        
        previous_url, next_url = previous_next_url(page)
        
        return render(request, 'blog/index.html', context={
            'is_paginated': is_paginated,
            'previous_url': previous_url,
            'next_url': next_url,
            'page': page,
        })




class PostDetail(ObjectDetailMixin, View):
    """ Обрабатывает отображение отдельного поста """
    model = Post
    template = 'blog/object_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """ Обрабатывает создание поста """
    form = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """ Обрабатывает редактирование поста """
    model = Post
    form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """ Обрабатывает удаление поста """
    model = Post
    redirect_url = 'posts_list_url'
    template = 'blog/post_delete_form.html'
    raise_exception = True


####################################################
# Контроллеры тегов
class TagsList(View):
    
    def get(self, request):
        tags = Tag.objects.all()

        paginator = Paginator(tags, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()
        previous_url = '?page={}'.format(page.previous_page_number()) if page.has_previous() else ''
        next_url = '?page={}'.format(page.next_page_number()) if page.has_next() else ''

        return render(request, 'blog/tags_list.html', context={
            'is_paginated': is_paginated,
            'previous_url': previous_url,
            'next_url': next_url,
            'page': page,
        })

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/object_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    redirect_url = 'tags_list_url'
    template = 'blog/tag_delete_form.html'
    raise_exception = True




