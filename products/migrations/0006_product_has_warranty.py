# Generated by Django 3.1.5 on 2021-02-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210212_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_warranty',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]