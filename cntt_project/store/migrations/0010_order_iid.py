# Generated by Django 4.1.3 on 2022-12-06 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_invoice_oid_remove_product_auid_author_pid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='iID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.invoice'),
        ),
    ]
