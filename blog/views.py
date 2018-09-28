from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectListMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Контроллеры постов
class PostsList(ObjectListMixin, View):
    """ Обрабатывает список постов """
    model = Post
    template = 'blog/object_list.html'


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
class TagsList(ObjectListMixin, View):
    model = Tag
    template = 'blog/object_list.html'


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



