# Generated by Django 4.2.4 on 2023-08-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_story_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
