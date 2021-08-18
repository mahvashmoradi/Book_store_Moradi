from django.contrib import admin

# Register your models here.
from .models import Invoice, InvoiceLine, Discount, Coupons

admin.site.register(Invoice)
admin.site.register(InvoiceLine)
admin.site.register(Discount)
admin.site.register(Coupons)
