# Generated by Django 3.0.3 on 2020-02-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20200215_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=50, unique=True, verbose_name='Stock Keeping Unit'),
        ),
    ]
