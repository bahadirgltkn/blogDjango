# Generated by Django 3.1.7 on 2021-06-21 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='created_date',
            new_name='createdDate',
        ),
    ]
