from django.views import generic
from .models import QuestionnaireExplanation, QuestionsData, QuestionnairesData, IDLinks, AnswersData
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

# def new_questionnaire(request, source, source_id, target, target_id)


class ExplanationView(generic.ListView):
    model = QuestionnaireExplanation
    template_name = 'questionnaire/explanation.html'
    context_object_name = 'explanations'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        source_in = self.request.resolver_match.kwargs['source']
        target_in = self.request.resolver_match.kwargs['target']
        x = QuestionnaireExplanation.objects.filter(
            source = source_in,
            target = target_in
        )
        y = QuestionnaireExplanation()
        y = x[0]
        y.source_id = self.request.resolver_match.kwargs['source_id']
        y.target_id = self.request.resolver_match.kwargs['target_id']
        return y


class QuestionnaireView(generic.ListView):
    questions = QuestionsData
    data = QuestionnairesData
    links = IDLinks

    template_name = 'questionnaire/questionnaire.html'

    context_object_name = 'questionnaire'

    def get_queryset(self):
        context = {
            'source': self.request.resolver_match.kwargs['source'],
            'source_id': self.request.resolver_match.kwargs['source_id'],
            'target': self.request.resolver_match.kwargs['target'],
            'target_id': self.request.resolver_match.kwargs['target_id'],
            'answers': AnswersData.objects.all()
        }
        # status: 1 = explanation
        # status: 2 = answer all questions
        if self.request.resolver_match.kwargs['status'] == 1:
            context['status'] = QuestionnaireExplanation.objects.filter(
                source = self.request.resolver_match.kwargs['source'],
                target = self.request.resolver_match.kwargs['target']
            )[0].explanation
        elif self.request.resolver_match.kwargs['status'] == 2:
            context['status'] = QuestionnaireExplanation.objects.filter(
                source='status',
                target='not_all_questions'
            )[0].explanation

        if context['source_id'] == context['target_id']:
            q = QuestionsData.objects.filter(target = '1') # self
        elif context['source_id'] == 'parent':
            q = QuestionsData.objects.filter(target = '2') # parent_child
        else:
            q = QuestionsData.objects.filter(target = '3') # teacher_child

        context['questions'] = q
        return context


def submitted(request, **kwargs):

    # get questionnaire information
    source = kwargs['source']
    source_id = kwargs['source_id']
    target = kwargs['target']
    target_id = kwargs['target_id']
    target_choice = 1
    if source == target:
        target_choice = 1
    elif source == 'parent' and target == 'child':
        target_choice = 2
    elif source == 'teacher' and target == 'child':
        target_choice = 3

    idl = IDLinks(source_id=source_id, target_id=target_id)
    questionnaire_id = idl.questionnaire_id

    # get questions/answers information
    number_of_questions = len(QuestionsData.objects.filter(target=target_choice))
    qds = []

    for k in request.POST.keys():
        key = k.split('_')
        if len(key) == 2:
            question_id = QuestionsData.objects.filter(question_number=key[0])[0]
            answer_id = AnswersData.objects.filter(answer_number=key[1])[0]
            qds.append(QuestionnairesData(questionnaire_id=questionnaire_id, question_id=question_id, answer_id=answer_id))

    if len(qds) == number_of_questions:
        # answered all questions
        # put in DB
        idl.save()
        for qd in qds:
            qd.save()
        # go to the appropriate page
        return HttpResponseRedirect(
            reverse('questionnaire:thankyou', args=[source, source_id, target, target_id]))
    else:
        return HttpResponseRedirect(
            reverse('questionnaire:questionnaire', args=[source, source_id, target, target_id, 2]))


# TODO
class ThankYouView(generic.ListView):
    template_name = 'questionnaire/thankyou.html'

    context_object_name = 'thankyou'

    def get_queryset(self):
        source = self.request.resolver_match.kwargs['source']
        source_id = self.request.resolver_match.kwargs['source_id']
        target = self.request.resolver_match.kwargs['target']
        target_id = self.request.resolver_match.kwargs['target_id']
        context = {
            'text': QuestionnaireExplanation.objects.filter(
                source='status',
                target='thankyou'
            )[0].explanation
        }

        if source == 'teacher':
            # go to "thank you" that leads to children
            context['whereto'] = 'teacher:children'
            context['what'] = source_id
        elif source == 'parent' and target == 'parent':
            context['whereto'] = 'parent:childquestionnaire'
            context['what'] = source_id
        elif source == 'parent' and target == 'child':
            context['whereto'] = 'parent:thankyou'
            context['what'] = source_id
        elif source == 'parent' and target == 'parent':
            # go to "thank you" that leads to Final Page
            pass

        return context
