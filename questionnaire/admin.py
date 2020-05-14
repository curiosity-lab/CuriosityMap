from django.contrib import admin

# Register your models here.
from .models import QuestionsData, AnswersData, QuestionnairesData, IDLinks, QuestionnaireExplanation

admin.site.register(QuestionsData)
admin.site.register(AnswersData)
admin.site.register(QuestionnairesData)
admin.site.register(IDLinks)
admin.site.register(QuestionnaireExplanation)