from django.contrib import admin
from .models import BookModel, CategoryModel, Author


# admin.site.register(BookModel)
# admin.site.register(CategoryModel)
# admin.site.register(Author)


# list_display= ('get_title',...)
# def get_title(self,obj):
#    categories= obj.category.all()
#    If categories :
#       return ','.join([str(category.title) for category in categories]
#   else:
#      return 'no category'
@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount_price', 'created', 'inventory', 'image']
    list_filter = ['categories']
    list_editable = ['price']
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    # list_filter = ['categories']
    # list_editable = ['name']
