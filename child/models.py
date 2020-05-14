from django.db import models

# Create your models here.
from teacher.models import *
from django.utils import timezone



GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('O', 'Other')
)


class ChildData(models.Model):
    teacher = models.ForeignKey(TeacherData, on_delete=models.CASCADE)
    child_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name_text = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='O')
    dob = models.DateField()

    def __str__(self):
        return self.name_text


class ParentData(models.Model):
    child = models.ForeignKey(ChildData, on_delete=models.CASCADE)
    parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name_text = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='O')
    age = models.PositiveIntegerField(default=20)
    consent = models.BooleanField(default=True)

    def __str__(self):
        return self.name_text

