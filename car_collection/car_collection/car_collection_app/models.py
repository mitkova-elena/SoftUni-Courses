from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from car_collection.car_collection_app.additional_functionality.validators import name_min_length_validator, \
    car_years_validator


class ProfileModel(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2
    MIN_AGE_REQUIRED = 18
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=([
            name_min_length_validator,
        ]
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        validators=([MinValueValidator(MIN_AGE_REQUIRED)]),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


SPORTS_CAR = "Sports Car"
PICKUP = "Pickup"
CROSSOVER = "Crossover"
MINIBUS = "Minibus"
OTHER = "Other"
CAR_TYPES = ((SPORTS_CAR, SPORTS_CAR),
             (PICKUP, PICKUP),
             (CROSSOVER, CROSSOVER),
             (MINIBUS, MINIBUS),
             (OTHER, OTHER),)


class CarModel(models.Model):
    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 2
    MAX_YEAR = 2019
    MIN_YEAR = 1980
    MIN_PRICE = 1

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=CAR_TYPES,
        null=False,
        blank=False,
    )
    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=[MinLengthValidator(MODEL_MIN_LENGTH)],
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        validators=[
            car_years_validator
        ],
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        validators=[MinValueValidator(MIN_PRICE)],
        null=False,
        blank=False,
    )
