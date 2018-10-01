from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time


class Post(models.Model):
    """ Модель поста """
    title = models.CharField(verbose_name='Заголовок', max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(verbose_name='Тело', blank=True, db_index=True)
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name='Теги')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """ Возвращает абсолютный URL поста """
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        """ Возвращает URL поста, который надо удалить. Написал для удобства в шаблонах """
        return reverse('post_delete_url', kwargs={'slug': self.slug})
    
    def get_update_url(self):
        """ Возвращает URL поста, который надо обновить """
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = '{}-{}'.format(slugify(self.title, allow_unicode=True), str(int(time())))
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-pub_date']


class Tag(models.Model):
    """ Модель тега """
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """ Возвращает абсолютный URL тега """
        return reverse('tag_detail_url', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        """ Возвращает URL тега, который надо удалить. Написал для удобства в шаблонах """
        return reverse('tag_delete_url', kwargs={'slug': self.slug})
    
    def get_update_url(self):
        """ Возвращает URL тега, который надо обновить """
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = '{}-{}'.format(slugify(self.title, allow_unicode=True), str(int(time())))
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['title']
    

