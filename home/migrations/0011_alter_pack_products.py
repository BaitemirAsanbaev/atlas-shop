# Generated by Django 4.1.2 on 2022-12-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_pack_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='products',
            field=models.ManyToManyField(blank=True, to='home.products'),
        ),
    ]
