# Generated by Django 2.2.4 on 2019-08-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='d', unique=True),
            preserve_default=False,
        ),
    ]
