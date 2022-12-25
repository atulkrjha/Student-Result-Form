# Generated by Django 4.1.4 on 2022-12-25 06:34

import django.core.validators
from django.db import migrations, models
import studentDetails.models


class Migration(migrations.Migration):

    dependencies = [
        ('studentDetails', '0002_alter_studentdetail_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultdetail',
            name='marksobt',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='resultdetail',
            name='maxmarks',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='dob',
            field=models.DateField(help_text='student DOB (B/W 1900 - 2018)', validators=[studentDetails.models.StudentDetail.validator_dob]),
        ),
    ]
