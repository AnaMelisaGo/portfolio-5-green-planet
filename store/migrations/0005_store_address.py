# Generated by Django 3.2 on 2022-11-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_businesstype_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='address',
            field=models.TextField(default='Abbey St'),
            preserve_default=False,
        ),
    ]
