from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from enum import Enum
from star_ratings.models import Rating
"""
Name - it should consist of a maximum of 30 characters.
Personal Pet Photo - the user can link a picture using a URL
The field date of birth is optional:
• Date of Birth - pet's day, month, and year of birth

Slug - a slug automatically generated using the pet's
 name and the pet's id, separated by a "-" (dash
"""

UserModel = get_user_model()


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class Choices(ChoicesMixin, Enum):
    VERY_BAD = 1
    BAD = 2
    NORMAL = 3
    GOOD = 4
    VERY_GOOD = 5


class Story(models.Model):
    date = models.DateField(
        blank=False,
        null=False,
    )

    overall = models.IntegerField(
        choices=Choices.choices(),
        default=Choices.NORMAL.value,
    )

    health = models.IntegerField(
        choices=Choices.choices(),
        default=Choices.NORMAL.value,
    )

    love = models.IntegerField(
        choices=Choices.choices(),
        default=Choices.NORMAL.value,
    )

    work = models.IntegerField(
        choices=Choices.choices(),
        default=Choices.NORMAL.value,
    )

    description = models.TextField(
        max_length=300,
        blank=True,
        null=True,
    )

    picture = models.URLField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(blank=True, null=True)

    favorite_story = models.BooleanField(default=False)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.date}")
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']
        constraints = [models.UniqueConstraint(fields=['user', 'date'], name='unique_user_date')]
