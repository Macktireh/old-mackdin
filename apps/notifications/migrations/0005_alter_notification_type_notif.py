# Generated by Django 3.2.12 on 2022-04-17 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_remove_notification_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='type_notif',
            field=models.CharField(choices=[('Like_Post', 'Like Post'), ('Add_Post', 'Add Post'), ('Add_Comment', 'Add Comment'), ('invitation_accepted', 'invitation accepted'), ('invitation_send', 'invitation send')], max_length=30, verbose_name='type_notif'),
        ),
    ]
