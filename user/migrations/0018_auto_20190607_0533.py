# Generated by Django 2.2 on 2019-06-07 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20190606_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='l_name',
        ),
    ]
