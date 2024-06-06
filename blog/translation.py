from modeltranslation.translator import translator, TranslationOptions, register
from .models import Post, Category, Tag


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
