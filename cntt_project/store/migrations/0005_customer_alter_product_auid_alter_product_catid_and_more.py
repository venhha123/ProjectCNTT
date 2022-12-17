# Generated by Django 4.1.3 on 2022-12-05 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_author_au_star_alter_product_book_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cusID', models.AutoField(primary_key=True, serialize=False)),
                ('cus_name', models.CharField(max_length=50)),
                ('cus_addr', models.CharField(max_length=50)),
                ('cus_phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='auID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.author'),
        ),
        migrations.AlterField(
            model_name='product',
            name='catID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oID', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('pID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('iID', models.AutoField(primary_key=True, serialize=False)),
                ('cusID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('oID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
        ),
    ]