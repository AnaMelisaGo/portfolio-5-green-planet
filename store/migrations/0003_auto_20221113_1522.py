# Generated by Django 3.2.16 on 2022-11-13 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20221113_0851'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='BusinessType',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='category',
            new_name='business_type',
        ),
    ]