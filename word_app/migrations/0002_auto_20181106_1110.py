# Generated by Django 2.1 on 2018-11-06 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordgame',
            old_name='date',
            new_name='dateval',
        ),
    ]