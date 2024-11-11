from django.contrib import admin
from .models import Blog, Category
from modeltranslation.admin import TranslationAdmin

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","category_name",)
    list_editable = ( "is_active",)
    search_fields = ("title","description",)
    readonly_fields = ("slug",)
    list_filter = ("category","is_active",)

    def category_name(self, obj):
        return obj.category.name

class CategoryAdmin(TranslationAdmin): 
    list_display = ('name',)


admin.site.register(Blog,BlogAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
