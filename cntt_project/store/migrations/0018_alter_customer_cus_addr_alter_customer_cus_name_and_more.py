# Generated by Django 4.1.3 on 2022-12-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_delete_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cus_addr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cus_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cus_phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]