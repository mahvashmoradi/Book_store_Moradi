from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, AddressModel, Customer, CityModel, ProvinceModel

# Register your models here.
# admin.site.register(CustomUser)
# admin.site.register(AddressModel)
# admin.site.register(Customer)
# admin.site.register(CityModel)
# admin.site.register(ProvinceModel)


@admin.register(AddressModel)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'province', 'city', 'address', 'postal_code', 'phone_number']
    # list_filter = ['province', 'city']
    fieldsets = (
        (None, {
            'fields': ('customer', 'province', 'city',),
            # 'classes': ('wide', 'extrapretty'),
        }),
        ('بیشتر', {
            'classes': ('collapse',),
            'fields': ('address', 'postal_code', 'phone_number'),
        }),
    )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user', 'gender', 'device', ]
    list_filter = ['gender', ]
    # list_editable = ['price']


@admin.register(ProvinceModel)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    # list_filter = ['gender', ]
    # list_editable = ['price']


@admin.register(CityModel)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    # list_filter = ['gender', ]
    # list_editable = ['price']
    search_fields = ['name', ]

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
