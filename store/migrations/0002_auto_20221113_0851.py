# Generated by Django 3.2.16 on 2022-11-13 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='store',
            old_name='store',
            new_name='store_name',
        ),
    ]