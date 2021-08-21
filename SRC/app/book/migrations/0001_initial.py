# Generated by Django 3.2.4 on 2021-08-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'نویسنده',
                'verbose_name_plural': 'نویسندگان',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('price', models.PositiveBigIntegerField(verbose_name='قیمت')),
                ('discount_price', models.PositiveBigIntegerField(default=0, verbose_name='قیمت با تخفیف')),
                ('created', models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت کتاب')),
                ('inventory', models.IntegerField(verbose_name='موجودی')),
                ('image', models.ImageField(default='0.png', null=True, upload_to='book/')),
                ('author', models.ManyToManyField(to='book.Author', verbose_name='نویسنده')),
                ('categories', models.ManyToManyField(related_name='category', to='book.CategoryModel', verbose_name='گروه')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب ها',
            },
        ),
    ]
