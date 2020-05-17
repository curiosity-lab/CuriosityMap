#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
import uuid

# Create your models here.
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('O', 'Other')
)

TEACHER_TYPES = (
    ('G', 'Grade'),
    ('T', 'Topic')
)

GRADES_CHOICES = (
    ('1st', 'א'),
    ('1st', '2')
)



class TeacherData(models.Model):
    teacher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")

    name_text = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='O')
    age = models.PositiveSmallIntegerField(default=20)

    city_text = models.CharField(max_length=200, default="")
    school_text = models.CharField(max_length=200, default="")
    teacher_type = models.CharField(max_length=5, choices=TEACHER_TYPES, default='G')

    grade = models.CharField(max_length=2, choices=GRADES_CHOICES, default='1st')
    topic = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name_text


class StatusData(models.Model):
    status_text = models.CharField(max_length=200, default="")
    status_number = models.PositiveSmallIntegerField(default=20)