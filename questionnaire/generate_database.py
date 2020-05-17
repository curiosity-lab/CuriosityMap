import sys
sys.path.insert(0, 'c:/Goren/CuriosityLab/Code/django/CuriosityMap/')

# tell django which settings module to use
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'CuriosityMap.settings.base'

import django
django.setup()

from questionnaire.models import QuestionnaireExplanation

qe1 = QuestionnaireExplanation(source='teacher', target='teacher', explanation='please fill the form on yourself.')
qe1.save()