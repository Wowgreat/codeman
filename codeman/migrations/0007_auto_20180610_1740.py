# Generated by Django 2.0.6 on 2018-06-10 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeman', '0006_group_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='post_man_id',
            new_name='post_man',
        ),
    ]
