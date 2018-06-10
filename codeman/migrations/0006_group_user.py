# Generated by Django 2.0.6 on 2018-06-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeman', '0005_user_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(related_name='users_of_group', through='codeman.UserGroup', to='codeman.User'),
        ),
    ]