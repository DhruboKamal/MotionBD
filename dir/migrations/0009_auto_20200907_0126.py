# Generated by Django 3.1 on 2020-09-06 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0008_auto_20200905_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motion',
            old_name='tournament_id',
            new_name='tournament',
        ),
    ]
