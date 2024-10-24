from django.contrib import admin
from. models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","category_name",)
    list_editable = ( "is_active",)
    search_fields = ("title","description",)
    readonly_fields = ("slug",)
    list_filter = ("category","is_active",)

    def category_name(self, obj):
        return obj.category.name

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)

# Register your models here.
