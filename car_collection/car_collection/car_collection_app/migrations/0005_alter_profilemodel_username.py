# Generated by Django 3.2.16 on 2022-10-30 10:32

import car_collection.car_collection_app.additional_functionality.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_collection_app', '0004_alter_profilemodel_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='username',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2), car_collection.car_collection_app.additional_functionality.validators.name_min_length_validator]),
        ),
    ]