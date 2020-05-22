import sys
sys.path.insert(0, 'c:/Goren/CuriosityLab/Code/django/CuriosityMap/')

# tell django which settings module to use
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'CuriosityMap.settings.base'

import django
django.setup()

from questionnaire.models import QuestionnaireExplanation, QuestionsData, AnswersData

generate_db = {
    'explanation': True,
    'questions': False,
    'answers': False
}

if generate_db['explanation']:
    # qe10 = QuestionnaireExplanation(source='teacher', target='teacher', explanation='Please fill the form on yourself.')
    # qe10.save()
    # qe11 = QuestionnaireExplanation(source='parent', target='parent', explanation='Please fill the form on yourself.')
    # qe11.save()
    # qe12 = QuestionnaireExplanation(source='parent', target='child', explanation='Please fill the form on your child.')
    # qe12.save()
    qe13 = QuestionnaireExplanation(source='teacher', target='child', explanation='Please fill the form on your student.')
    qe13.save()
    # qe2 = QuestionnaireExplanation(source='status', target='not_all_questions', explanation='Please answer all questions.')
    # qe2.save()
    # qe3 = QuestionnaireExplanation(source='status', target='thankyou', explanation='Thank you for filling the questionnaire.')
    # qe3.save()


if generate_db['questions']:
    the_questions = [
        'Q1',
        'Q2'
    ]
    for i, q in enumerate(the_questions):
        QuestionsData(question_number=i + 1, name_text=q, target=1).save()
        QuestionsData(question_number=i + 1, name_text=q, target=2).save()
        QuestionsData(question_number=i + 1, name_text=q, target=3).save()

if generate_db['answers']:
    ANSWERS_CHOICES = [
        (1, 'בכלל לא מתאר אותי'),
        (2, 'מתאר אותי במידה מעטה מאוד'),
        (3, 'מתאר אותי במידה מעטה'),
        (4, 'מתאר אותי במידה בינונית'),
        (5, 'מתאר אותי במידה רבה'),
        (6, 'מתאר אותי במידה רבה מאוד'),
        (7, 'מתאר אותי באופן מלא (לגמרי אני)')
    ]
    for a in ANSWERS_CHOICES:
        AnswersData(name_text=a[1], answer_number=a[0]).save()




