# Generated by Django 4.1.2 on 2022-12-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
