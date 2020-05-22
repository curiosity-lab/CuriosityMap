from django.db import models

# Create your models here.
from teacher.models import *
import uuid
import datetime


GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('O', 'Other')
)


class ChildData(models.Model):
    child_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(TeacherData, on_delete=models.CASCADE)

    name_text = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='O')
    dob = models.DateField(default=datetime.date.today)

    parent_q = models.BooleanField(default=False)
    child_q = models.BooleanField(default=False)
    self_q = models.BooleanField(default=False)
    teacher_q = models.BooleanField(default=False)

    def __str__(self):
        return self.name_text


class ParentData(models.Model):
    parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    child = models.ForeignKey(ChildData, on_delete=models.CASCADE)

    name_text = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='O')
    age = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.name_text


class StatusData(models.Model):
    status_text = models.CharField(max_length=200, default="")
    status_number = models.PositiveSmallIntegerField(default=20)