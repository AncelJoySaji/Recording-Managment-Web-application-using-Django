# Generated by Django 3.2.3 on 2021-06-21 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20210619_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='id',
        ),
        migrations.AlterField(
            model_name='album',
            name='Album_title',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
