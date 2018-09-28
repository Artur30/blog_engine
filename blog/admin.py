from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'body', 'tags']
    prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

