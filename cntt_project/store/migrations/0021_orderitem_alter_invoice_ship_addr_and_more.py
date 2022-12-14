# Generated by Django 4.1.3 on 2022-12-21 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_order_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('oID', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField(default=0, null=True)),
                ('comment', models.TextField(max_length=254, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ship_addr',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='book_name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='iID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.invoice'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='pID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
