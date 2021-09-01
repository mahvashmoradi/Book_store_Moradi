from django.contrib import admin
from .models import CustomUser, AddressModel, Customer, CityModel, ProvinceModel
# Register your models here.
admin.site.register(CustomUser)
# admin.site.register(AddressModel)
admin.site.register(Customer)
admin.site.register(CityModel)
admin.site.register(ProvinceModel)

@admin.register(AddressModel)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'province', 'city', 'address', 'postal_code', 'phone_number']
    list_filter = ['province','city' ]
    # list_editable = ['price']
#
# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         disabled_fields = set()  # type: Set[str]
#
#         if not is_superuser:
#             disabled_fields |= {
#                 'username',
#                 'is_superuser',
#             }
#
#         for f in disabled_fields:
#             if f in form.base_fields:
#                 form.base_fields[f].disabled = True
#
#         return form