# Generated by Django 4.2.4 on 2023-08-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_story_picture_alter_story_user'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='story',
            constraint=models.UniqueConstraint(fields=('user', 'date'), name='unique_user_date'),
        ),
    ]
