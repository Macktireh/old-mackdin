# Generated by Django 3.2.12 on 2022-04-11 13:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_rename_like_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
