# Generated by Django 4.2.4 on 2023-08-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='diaryuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
