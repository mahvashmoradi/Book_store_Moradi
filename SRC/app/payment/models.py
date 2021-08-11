from django.db import models
from app.accounts.models import CustomUser, Customer


# from app.book.models import BookModel


# Create your models here.
# Discount Code which decrease price on value
class DiscountCodeValue(models.Model):
    class Meta:
        verbose_name = 'کد تخفیف نقدی'
        verbose_name_plural = 'کدهای تخفیف نقدی'

    started = models.DateTimeField('زمان شروع', )
    finished = models.DateTimeField('زمان پایان', )
    code = models.CharField('کد تخفیف', blank=False, max_length=10)
    amount = models.FloatField()

    def __str__(self):
        return self.code


# Discount Code which decrease price on percent
class DiscountCodePercent(models.Model):
    class Meta:
        verbose_name = 'کد تخفیف درصدی'
        verbose_name_plural = 'کدهای تخفیف درصدی'

    started = models.DateTimeField('زمان شروع', )
    finished = models.DateTimeField('زمان پایان', )
    code = models.CharField('کد تخفیف', blank=False, max_length=10)
    percent = models.FloatField()

    def __str__(self):
        return self.code


# Discount on price of book with value
class DiscountValue(models.Model):
    class Meta:
        verbose_name = 'تخفیف نقدی'
        verbose_name_plural = 'تخفیف های نقدی'

    book = models.ForeignKey('book.BookModel', on_delete=models.CASCADE, related_name='dis_value',
                             verbose_name='نام کتاب')
    value = models.DecimalField('مقدارتخفیف', max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.book)


# Discount on price of book with percent
class DiscountPercent(models.Model):
    class Meta:
        verbose_name = 'تخفیف درصدی'
        verbose_name_plural = 'تخفیف های درصدی'

    book = models.ForeignKey('book.BookModel', on_delete=models.CASCADE, related_name='dis_percent',
                             verbose_name='نام محصول')
    percent = models.IntegerField('درصد تخفیف', )

    def __str__(self):
        return str(self.book)


# Invoice(factor)
class Invoice(models.Model):
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    ORDER = 'O'
    COMPLETE = 'C'
    INVOICE_CHOICES = [(ORDER, 'سفارش'), (COMPLETE, 'آماده ارسال')]
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='invoices', verbose_name='کاربر')
    invoice_date = models.DateTimeField('تاریخ سفارش', auto_now_add=True)
    invoice_complete_date = models.DateTimeField('تاریخ تکمیل سفارش', )
    total = models.BigIntegerField('مجموع', )
    total_with_discount = models.BigIntegerField('قابل پرداخت', blank=True, null=True)
    status = models.CharField(choices=INVOICE_CHOICES, max_length=1, default=ORDER, verbose_name='وضعیت سفارش')
    discount_value = models.ForeignKey(DiscountCodeValue, blank=True, null=True, on_delete=models.DO_NOTHING,
                                       related_name='value_code_discount')
    discount_percent = models.ForeignKey(DiscountCodePercent, blank=True, null=True, on_delete=models.DO_NOTHING,
                                         related_name='percent_code_discount')

    def __str__(self):
        return str(self.id)

    def calculate(self):
        qs_percent = DiscountCodePercent.objects.filter(finished__gte=self.invoice_complete_date,
                                                        started__lte=self.invoice_complete_date)
        qs_value = DiscountCodeValue.objects.filter(finished__gte=self.invoice_complete_date,
                                                    started__lte=self.invoice_complete_date)
        total = self.total
        if qs_percent:
            total = (100 - qs_percent.values('percent')[0]['percent']) * total / 100
            self.discount_percent = DiscountCodePercent.objects.get(finished__gte=self.invoice_complete_date,
                                                                    started__lte=self.invoice_complete_date)
            self.save()

        if qs_value:
            total = total - qs_value.values('amount')[0]['amount']
            self.discount_value = DiscountCodeValue.objects.get(finished__gte=self.invoice_complete_date,
                                                                started__lte=self.invoice_complete_date)
            self.save()

        self.total_with_discount = total

        # self.save()
        return self.total_with_discount


# Item in Invoice (factor detail)
class InvoiceLine(models.Model):
    class Meta:
        verbose_name = 'جزییات سفارش'
        verbose_name_plural = 'جزییات سفارش'

    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, verbose_name='شماره فاکتور')
    book = models.ForeignKey('book.BookModel', on_delete=models.DO_NOTHING, verbose_name='محصول')
    unit_price = models.IntegerField('قیمت واحد', )
    quantity = models.IntegerField('تعداد', )

    def __str__(self):
        return str(self.invoice)
