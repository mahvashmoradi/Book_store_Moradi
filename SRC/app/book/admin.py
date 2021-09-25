from django.contrib import admin
from .models import BookModel, CategoryModel, Author

# admin.site.register(BookModel)
# admin.site.register(CategoryModel)
# admin.site.register(Author)
from django.core import serializers
from django.http import HttpResponse


@admin.action(description='receive selected book as json')
def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount_price', 'created', 'inventory', 'get_title']
    list_filter = ['categories']
    list_editable = ['price']
    actions = [export_as_json]

    # prepopulated_fields = {'slug': ('name',)}
    # list_display= ('get_title',...)

    def get_title(self, obj):
        categories = obj.categories.all()
        if categories:
            return ','.join([str(category.name) for category in categories])
        else:
            return 'no category'


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_items', ]
    # prepopulated_fields = {'slug': ('name',)}
    # search_fields = ['get_items', ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    # list_filter = ['categories']
    # list_editable = ['name']
