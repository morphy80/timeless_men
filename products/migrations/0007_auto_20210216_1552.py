# Generated by Django 3.1.5 on 2021-02-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_has_warranty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='year_warranty',
            field=models.CharField(choices=[('1', 'none'), ('2', '2 years'), ('3', '3 years'), ('5', '5 years'), ('l', 'life')], default='1', max_length=1),
        ),
    ]