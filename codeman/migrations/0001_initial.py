# Generated by Django 2.0.6 on 2018-06-08 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('is_show', models.BooleanField(default=False)),
                ('id_del', models.BooleanField(default=False)),
                ('helped_number', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'codeman_articles',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('intro', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'codeman_groups',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('intro', models.CharField(blank=True, default='', max_length=300)),
                ('avatar', models.CharField(blank=True, default='http://www.sucaijishi.com/uploadfile/2016/0203/20160203022635285.png', max_length=200)),
                ('occupation', models.CharField(blank=True, default='保密', max_length=100)),
                ('is_show_location', models.BooleanField(default=False)),
                ('company_or_school', models.CharField(blank=True, default='保密', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('highlighted', models.TextField()),
            ],
            options={
                'db_table': 'codeman_users',
                'ordering': ('created_at',),
            },
        ),
        migrations.AddField(
            model_name='group',
            name='create_man_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_groups', to='codeman.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='group_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='codeman.Group'),
        ),
        migrations.AddField(
            model_name='article',
            name='post_man_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeman.User'),
        ),
    ]
