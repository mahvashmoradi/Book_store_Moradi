# Generated by Django 3.2.4 on 2021-09-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
    ]
