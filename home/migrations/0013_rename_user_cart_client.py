# Generated by Django 4.1.2 on 2022-12-06 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='client',
        ),
    ]
