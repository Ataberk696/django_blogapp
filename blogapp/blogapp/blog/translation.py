from modeltranslation.translator import register, TranslationOptions
from .models import Category
from .models import Blog

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',) 


