from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectListMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm


# Контроллеры постов
class PostsList(ObjectListMixin, View):
    """ Обрабатывает список постов """
    model = Post
    template = 'blog/index.html'


class PostDetail(ObjectDetailMixin, View):
    """ Обрабатывает отображение отдельного поста """
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    """ Обрабатывает создание поста """
    form = PostForm
    template = 'blog/post_create_form.html'


class PostUpdate(ObjectUpdateMixin, View):
    """ Обрабатывает редактирование поста """
    model = Post
    form = PostForm
    template = 'blog/post_update_form.html'


class PostDelete(ObjectDeleteMixin, View):
    """ Обрабатывает удаление поста """
    model = Post
    redirect_url = 'posts_list_url'
    template = 'blog/post_delete_form.html'


####################################################
# Контроллеры тегов
class TagsList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tags_list.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    form = TagForm
    template = 'blog/tag_update_form.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    redirect_url = 'tags_list_url'
    template = 'blog/tag_delete_form.html'



