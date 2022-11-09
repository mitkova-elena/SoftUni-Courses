# Generated by Django 3.2.16 on 2022-10-30 07:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(18)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
