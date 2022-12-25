from django.db import models
from django.db.models import Model
from django import forms
# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

import re





class StudentDetail(models.Model):

    studentclasschoices = [
        ('Grade 6','grade_6'),
        ('Grade 7','grade_7'),
        ('Grade 8','grade_8'),
        ('Grade 9','grade_9'),
        ('Grade 10','grade_10'),
        ('Grade 11','grade_11'),
        ('Grade 12','grade_12')
    ]

    genderchoices = [
        ('Male', 'male'),
        ('Female', 'female'),
        ('Do not disclose', 'dnd'),
        ('others', 'oth')
    ]

    
    def validator_num(value):
        if not value.isnumeric():
            raise ValidationError(
                _('%(value)s is not a number'),
                params={'value': value},
            )

    def validator_mob(value):

        phone_regex = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'

        if not re.search(phone_regex, value):
            raise ValidationError(
                _('%(value)s is not a valid mobile number'),
                params={'value': value},
            )

    def validator_dob(value):

        #print(type(value.year))

        if not value.year in list(range(1900, date.today().year-4)):
            raise ValidationError(
                _('%(value)s should be between year 1900 and %(value2)s'),
                params={'value': value, 'value2':(date.today().year-4)},
            )


    name = models.CharField(max_length=40, null=False, blank=False, help_text=_("student name"))
    studentclass = models.CharField(max_length= 100, choices = studentclasschoices, help_text=_("student class"))
    rollno = models.CharField(max_length= 100, validators=[validator_num], help_text=_("student roll number"), unique=True, null = False, blank = False)
    dob = models.DateField(null = False, blank = False, validators= [validator_dob], help_text=_("student DOB (B/W 1900 - 2018)"))
    gender = models.CharField(max_length= 100, choices=genderchoices)
    mobilenumber = models.CharField(max_length= 100, validators=[validator_mob], help_text=_("student mobile number"), null = False, blank = False)
    
    def __str__(self):
        return "Name : {}  Roll No. : {}".format(self.name, self.rollno)





class ResultDetail(models.Model):
    subjectchoices = [
        ('English', 'english'),
        ('Mathematics', 'mathematics'),
        ('Science','science'),
        ('Social Studies', 'social_studies')
    ]


    student = models.ForeignKey(StudentDetail, related_name="results", on_delete=models.DO_NOTHING)
    subject =  models.CharField(max_length= 100, choices=subjectchoices)
    maxmarks = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)])
    marksobt = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    remarks = models.CharField(max_length= 1000)

    class Meta:
        unique_together = ('student', 'subject',)

    def clean(self) -> None:
        if self.marksobt <= self.maxmarks:
            self.is_cleaned = True
        else:
            print("here4")
            raise ValidationError(
                _('%(value)s should be less than Maxvalue : %(maxvalue)s'),
                params={'value': self.marksobt, 'maxvalue': (self.maxmarks if self.maxmarks>0 else 0)},
            )
    

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            print("here3")
            self.clean()


        super().save(*args, **kwargs)

    
        



