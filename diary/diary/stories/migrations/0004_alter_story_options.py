# Generated by Django 4.2.4 on 2023-08-08 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_alter_story_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ['-date']},
        ),
    ]
