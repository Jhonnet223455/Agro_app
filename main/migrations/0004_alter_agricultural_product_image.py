# Generated by Django 4.2.7 on 2023-11-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_agricultural_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agricultural_product',
            name='image',
            field=models.ImageField(upload_to='static/uploads/'),
        ),
    ]
