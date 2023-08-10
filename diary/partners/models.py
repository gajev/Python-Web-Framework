from enum import Enum

from django.db import models

from diary.stories.models import ChoicesMixin


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class Choices(ChoicesMixin, Enum):
    LIFE_COACH = 1
    DOCTOR = 2
    LOVE_COACH = 3
    JOB_COACH = 4


class PartnerUser(models.Model):

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=30
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    phone_number = models.IntegerField(
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=False,
        blank=False,
    )

    type_partner = models.IntegerField(
        choices=Choices.choices(),
    )



