# Generated by Django 4.1.3 on 2022-12-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_invoice_place_status_alter_invoice_date_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='book_description',
            field=models.TextField(null=True),
        ),
    ]
