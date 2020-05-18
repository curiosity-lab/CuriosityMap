#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.db import models
import uuid

TARGET_CHOICES = {
    ('1', 'self'),
    ('2', 'parent_child'),
    ('3', 'teacher_child')
}


# list of explanations
class QuestionnaireExplanation(models.Model):
    source = models.CharField(max_length=200, default="")
    target = models.CharField(max_length=200, default="")
    source_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    target_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    explanation = models.CharField(max_length=200, default="")


# a list of the questionnaires questions (25 questions)
class QuestionsData(models.Model):
    name_text = models.CharField(max_length=200, default="")
    target = models.CharField(max_length=200, choices=TARGET_CHOICES, default='1')
    question_number = models.IntegerField(default=0)


# a list of the 7-Likert scane answers
class AnswersData(models.Model):
    name_text = models.CharField(max_length=200, default="")
    answer_number = models.IntegerField(default=0)


# Answers data: question, answer, questionnaire id
class QuestionnairesData(models.Model):
    question_id= models.ForeignKey(QuestionsData, on_delete=models.CASCADE, default=0)
    answer_id = models.ForeignKey(AnswersData, on_delete=models.CASCADE, default=0)
    questionnaire_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)


# linking between questionnaire, who filled it (source) on whom (target)
# source/target can be teacher/child/parent
class IDLinks(models.Model):
    questionnaire_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    source_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    target_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)

