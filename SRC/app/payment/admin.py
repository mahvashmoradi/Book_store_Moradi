from django.contrib import admin

# Register your models here.
from .models import Invoice, InvoiceLine, DiscountValue, DiscountPercent,\
    DiscountCodeValue, DiscountCodePercent

admin.site.register(Invoice)
admin.site.register(InvoiceLine)
admin.site.register(DiscountCodeValue)
admin.site.register(DiscountCodePercent)
admin.site.register(DiscountValue)
admin.site.register(DiscountPercent)