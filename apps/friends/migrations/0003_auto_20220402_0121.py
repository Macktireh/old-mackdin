# Generated by Django 3.2.12 on 2022-04-01 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_alter_relationship_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='date_received',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='date_sender',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]