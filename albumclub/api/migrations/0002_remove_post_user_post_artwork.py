# Generated by Django 4.1.6 on 2023-02-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='artwork',
            field=models.URLField(default='No Art Work'),
            preserve_default=False,
        ),
    ]
