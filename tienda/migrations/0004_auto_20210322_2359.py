# Generated by Django 3.1.7 on 2021-03-23 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_auto_20210322_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriaproducto',
            old_name='update',
            new_name='updated',
        ),
    ]
