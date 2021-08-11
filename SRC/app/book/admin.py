from django.contrib import admin
from .models import BookModel, CategoryModel, Author, Store
# Register your models here.
admin.site.register(BookModel)
admin.site.register(CategoryModel)
admin.site.register(Author)
admin.site.register(Store)
# list_display= ('get_title',...)
# def get_title(self,obj):
#    categories= obj.category.all()
#    If categories :
#       return ','.join([str(category.title) for category in categories]
#   else:
#      return 'no category'
