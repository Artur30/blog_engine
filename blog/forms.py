from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        new_title = self.cleaned_data['title']

        if Tag.objects.filter(title__iexact=new_title).count():
            raise ValidationError('Заголовок тега "{}" уже существует...'.format(new_title))
        return new_title


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        new_title = self.cleaned_data['title']

        if Post.objects.filter(title__iexact=new_title).count():
            raise ValidationError('Заголовок поста "{}" уже существует...'.format(new_title))
        return new_title


