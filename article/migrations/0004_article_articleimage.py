# Generated by Django 3.1.7 on 2021-06-24 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210623_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articleImage',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name=' Add photo to article '),
        ),
    ]