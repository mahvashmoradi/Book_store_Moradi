# Generated by Django 3.2.4 on 2021-09-02 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('payment', '0002_auto_20210901_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoice_issued', to='accounts.addressmodel', verbose_name='آدرس'),
        ),
    ]
