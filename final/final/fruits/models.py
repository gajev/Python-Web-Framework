from django.core import validators
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


def check_first_letter_is_alpha(some_string):
    if not some_string[0].isalpha():
        raise validators.ValidationError("Your name must start with a letter!")


def check_string_is_alpha_only(some_string):
    for ch in some_string:
        if not ch.isalpha():
            raise validators.ValidationError("Fruit name should contain only letters!")
# Create your models here.


class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 25
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_LAST_NAME = 35
    MIN_LEN_LAST_NAME = 1
    MAX_LEN_EMAIL = 40
    MAX_LEN_PASSWORD = 20
    MIN_LEN_PASSWORD = 8

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_FIRST_NAME,
        verbose_name="First Name",
        validators=[
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            check_first_letter_is_alpha,
        ],
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_LAST_NAME,
        verbose_name="Last Name",
        validators=[
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            check_first_letter_is_alpha,
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=MAX_LEN_EMAIL,
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PASSWORD,
        validators=[
            validators.MinLengthValidator(MIN_LEN_PASSWORD),
        ],
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name="Image URL"
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18
    )


class Fruit(models.Model):
    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2

    name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LEN_NAME),
            check_string_is_alpha_only,
        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )


class MyDiaryUserManager(auth.models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class MyDiaryUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    objects = MyDiaryUserManager()
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

