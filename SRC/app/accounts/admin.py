from django.contrib import admin
from .models import CustomUser, AddressModel, Customer, CityModel, ProvinceModel
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AddressModel)
admin.site.register(Customer)
admin.site.register(CityModel)
admin.site.register(ProvinceModel)
