# Generated by Django 4.2.5 on 2023-10-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
