from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    """ Модель поста """
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        """ Возвращает абсолютный URL поста """
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    

class Tag(models.Model):
    """ Модель тега """
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        """ Возвращает абсолютный URL тега """
        return reverse('tag_detail_url', kwargs={'slug': self.slug})


