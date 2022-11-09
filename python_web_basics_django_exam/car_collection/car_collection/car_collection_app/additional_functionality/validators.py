from django.core.validators import MinLengthValidator
from django.core import exceptions


def name_min_length_validator(value):
    USERNAME_MIN_LENGTH = 2
    if len(value) < USERNAME_MIN_LENGTH:
        raise exceptions.ValidationError("The username must be a minimum of 2 chars")


def car_years_validator(value):
    MAX_YEAR = 2019
    MIN_YEAR = 1980

    if value > MAX_YEAR or value < MIN_YEAR:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")
