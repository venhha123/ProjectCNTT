# Generated by Django 4.1.3 on 2022-12-11 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
