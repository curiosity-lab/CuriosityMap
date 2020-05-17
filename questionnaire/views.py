from django.shortcuts import render
from django.views import generic
from .models import QuestionnaireExplanation, QuestionsData, QuestionnairesData, IDLinks, AnswersData

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


class QuestionnaireView(generic.TemplateView):
    questions = QuestionsData
    data = QuestionnairesData
    links = IDLinks

    template_name = 'questionnaire/questionnaire.html'

    context_object_name = 'questionnaire'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    #     context['modelone'] = ModelOne.objects.get(*query
    #     logic *)
    #     context['modeltwo'] = ModelTwo.objects.get(*query
    #     logic *)
    #     return context
    #
    # def get_queryset(self):
        source_in = self.request.resolver_match.kwargs['source']
        target_in = self.request.resolver_match.kwargs['target']

        if source_in == target_in:
            q = QuestionsData.objects.filter(target = '1') # self
        elif source_in == 'parent':
            q = QuestionsData.objects.filter(target = '2') # parent_child
        else:
            q = QuestionsData.objects.filter(target = '3') # teacher_child

        context['questions'] = QuestionsData.objects.filter(question_number = q[0])
        context['answers'] = AnswersData.objects.select_all()
        return context
        # try:
        #     return QuestionsData.objects.filter(
        #         question_number = q[0]
        #     )
        # except:
        #     return QuestionsData.objects.filter()

