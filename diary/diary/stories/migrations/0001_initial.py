# Generated by Django 4.2.4 on 2023-08-08 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('overall', models.IntegerField(choices=[(1, 'VERY_BAD'), (2, 'BAD'), (3, 'NORMAL'), (4, 'GOOD'), (5, 'VERY_GOOD')], default=3)),
                ('health', models.IntegerField(choices=[(1, 'VERY_BAD'), (2, 'BAD'), (3, 'NORMAL'), (4, 'GOOD'), (5, 'VERY_GOOD')], default=3)),
                ('love', models.IntegerField(choices=[(1, 'VERY_BAD'), (2, 'BAD'), (3, 'NORMAL'), (4, 'GOOD'), (5, 'VERY_GOOD')], default=3)),
                ('work', models.IntegerField(choices=[(1, 'VERY_BAD'), (2, 'BAD'), (3, 'NORMAL'), (4, 'GOOD'), (5, 'VERY_GOOD')], default=3)),
                ('description', models.TextField(max_length=300)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('favorite_story', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
