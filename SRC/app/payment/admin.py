from django.contrib import admin

# Register your models here.
from .models import Invoice, InvoiceLine, Discount, Coupons

# admin.site.register(Invoice)
# admin.site.register(InvoiceLine)
# admin.site.register(Discount)
# admin.site.register(Coupons)


class InvoiceInLineAdmin(admin.TabularInline):
    model = InvoiceLine
    list_display = ['invoice', 'items', 'quantity']
    # list_filter = ['invoice']
    readonly_fields = ('invoice', 'items', 'quantity')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['customer', 'invoice_complete_date', 'total', 'status', ]
    list_filter = ['customer']
    inlines = (InvoiceInLineAdmin,)
    # list_editable = ['price']
    # readonly_fields = ['name']


admin.site.register(Invoice, InvoiceAdmin)


@admin.register(InvoiceLine)
class InvoiceLineAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'items', 'quantity']
    list_filter = ['invoice']
    readonly_fields = ('invoice', 'items', 'quantity')


# admin.site.register(InvoiceLine, InvoiceLineAdmin)

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['book', 'choice_discount', 'value', 'percent', ]
    list_filter = ['choice_discount']
    list_editable = [ 'choice_discount', 'value', 'percent',]
    # readonly_fields = ['name']


@admin.register(Coupons)
class CouponsAdmin(admin.ModelAdmin):
    list_display = ['code', 'started', 'finished', 'choice_discount', 'value', 'percent', ]
    list_filter = ['finished']
    list_editable = ['finished', 'choice_discount', 'value', 'percent', ]
    # readonly_fields = ['name']
