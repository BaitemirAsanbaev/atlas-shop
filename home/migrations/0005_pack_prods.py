# Generated by Django 4.1.2 on 2022-11-30 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_pack_products_pack_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack',
            name='prods',
            field=models.ManyToManyField(to='home.pack'),
        ),
    ]
