from django.contrib import admin
from .models import Post, Comment, Tag, Category
from modeltranslation.admin import TranslationAdmin


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'content', 'author', 'slug')


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = ('name',)


admin.site.register(Comment)
