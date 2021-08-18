# Generated by Django 3.2.4 on 2021-08-15 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.DateTimeField(verbose_name='زمان شروع')),
                ('finished', models.DateTimeField(verbose_name='زمان پایان')),
                ('code', models.CharField(max_length=10, verbose_name='کد تخفیف')),
                ('value', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مقدار تخفیف')),
                ('percent', models.FloatField(blank=True, null=True, verbose_name='درصد تخفیف')),
                ('choice_discount', models.CharField(choices=[('V', 'مقدار'), ('P', 'درصدی')], default='V', max_length=1, verbose_name='نوع تخفیف')),
            ],
            options={
                'verbose_name': 'کد تخفیف نقدی',
                'verbose_name_plural': 'کدهای تخفیف نقدی',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')),
                ('invoice_complete_date', models.DateTimeField(verbose_name='تاریخ تکمیل سفارش')),
                ('total', models.PositiveBigIntegerField(verbose_name='مجموع')),
                ('total_with_discount', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='قابل پرداخت')),
                ('status', models.CharField(choices=[('O', 'سفارش'), ('C', 'آماده ارسال')], default='O', max_length=1, verbose_name='وضعیت سفارش')),
                ('check_discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='value_code_discount', to='payment.coupons')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoices', to='accounts.customer', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.PositiveIntegerField(verbose_name='قیمت واحد')),
                ('quantity', models.IntegerField(verbose_name='تعداد')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book.bookmodel', verbose_name='محصول')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Items', to='payment.invoice', verbose_name='شماره فاکتور')),
            ],
            options={
                'verbose_name': 'جزییات سفارش',
                'verbose_name_plural': 'جزییات سفارش',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مقدارتخفیف')),
                ('percent', models.FloatField(blank=True, null=True, verbose_name='درصد تخفیف')),
                ('choice_discount', models.CharField(choices=[('V', 'مقدار'), ('P', 'درصدی')], default='V', max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dis_value', to='book.bookmodel', verbose_name='نام کتاب')),
            ],
            options={
                'verbose_name': 'تخفیف نقدی',
                'verbose_name_plural': 'تخفیف های نقدی',
            },
        ),
    ]
