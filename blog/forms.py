from django import forms
from .models import Tag
from django.core.exceptions import ValidationError


class TagForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=50)
    slug = forms.CharField(label='Slug', max_length=50)

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})

    def clean_slug(self):
        new_slug = self.cleaned_data['slug']

        # slug не может быть create так как по URL blog/tag/create будет форма
        if new_slug == 'create':
            raise ValidationError('Slug не может называться "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug "{}" уже существует'.format(new_slug))

        return new_slug
    

    def save(self):
        new_tag = Tag.objects.create(title=self.cleaned_data['title'], slug=self.cleaned_data['slug'])
        return new_tag

