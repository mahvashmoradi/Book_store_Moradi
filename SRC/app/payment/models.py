from django.db import models
from app.accounts.models import CustomUser, Customer


# from app.book.models import BookModel


# Create your models here.
# Coupons Code which decrease total price of factor
class Coupons(models.Model):
    VALUE = 'V'
    PERCENT = 'P'
    DISCOUNT_CHOICES = [(VALUE, 'مقدار'), (PERCENT, 'درصدی')]
    started = models.DateTimeField('زمان شروع', )
    finished = models.DateTimeField('زمان پایان', )
    code = models.CharField('کد تخفیف', blank=False, max_length=10)
    value = models.PositiveBigIntegerField('مقدار تخفیف', blank=True, null=True)
    percent = models.FloatField('درصد تخفیف', blank=True, null=True)
    choice_discount = models.CharField('نوع تخفیف', choices=DISCOUNT_CHOICES, max_length=1, default=VALUE)

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کدهای تخفیف'

    def __str__(self):
        return self.code


# Discount on price of book with value and percent
class Discount(models.Model):
    book = models.ForeignKey('book.BookModel', on_delete=models.CASCADE, related_name='dis_value',
                             verbose_name='نام کتاب')
    value = models.PositiveBigIntegerField('مقدارتخفیف', blank=True, null=True)
    percent = models.FloatField('درصد تخفیف', blank=True, null=True)
    choice_discount = models.CharField(choices=Coupons.DISCOUNT_CHOICES, max_length=1, default=Coupons.VALUE)

    class Meta:
        verbose_name = 'تخفیف محصول'
        verbose_name_plural = 'تخفیف محصولات'

    def __str__(self):
        return str(self.book)


# Invoice(factor)
class Invoice(models.Model):
    ORDER = 'O'
    COMPLETE = 'C'
    INVOICE_CHOICES = [(ORDER, 'سفارش'), (COMPLETE, 'آماده ارسال')]
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='invoices', verbose_name='کاربر')
    invoice_date = models.DateTimeField('تاریخ سفارش', auto_now_add=True)
    invoice_complete_date = models.DateTimeField('تاریخ تکمیل سفارش',blank=True, null=True )
    total = models.PositiveBigIntegerField('مجموع',blank=True, null=True )
    total_with_discount = models.PositiveBigIntegerField('قابل پرداخت', blank=True, null=True)
    status = models.CharField(choices=INVOICE_CHOICES, max_length=1, default=ORDER, verbose_name='وضعیت سفارش')
    check_discount = models.ForeignKey(Coupons, blank=True, null=True, on_delete=models.DO_NOTHING,
                                       related_name='coupons_code')

    def calculate(self):
        qs_value = Coupons.objects.filter(finished__gte=self.invoice_complete_date,
                                          started__lte=self.invoice_complete_date)
        total = self.total
        data = {'qs': qs_value}
        # if qs_percent:
        #     total = (100 - qs_percent.values('percent')[0]['percent']) * total / 100
        #     self.discount_percent = DiscountCodePercent.objects.get(finished__gte=self.invoice_complete_date,
        #                                                             started__lte=self.invoice_complete_date)
        #     self.save()

        if qs_value:
            if 'qs' == Coupons.VALUE:
                total = total - qs_value.values('amount')[0]['amount']
            else:
                total = (100 - qs_value.values('percent')[0]['percent']) * total / 100

        self.total_with_discount = total
        self.save()
        return self.total_with_discount

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def __str__(self):
        return str(self.id)


# Item in Invoice (factor detail)
class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='Items', verbose_name='شماره فاکتور')
    items = models.ForeignKey('book.BookModel', on_delete=models.DO_NOTHING, verbose_name='محصول')
    unit_price = models.PositiveIntegerField('قیمت واحد', )
    quantity = models.IntegerField('تعداد', )

    def add_to_cart(self):
        return self.id

    class Meta:
        verbose_name = 'جزییات سفارش'
        verbose_name_plural = 'جزییات سفارش'

    def __str__(self):
        return str(self.invoice)
