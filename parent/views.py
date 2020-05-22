from django.shortcuts import render
from django.views import generic
from .models import ParentData, ChildData, StatusData
from teacher.models import TeacherData
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .forms import ChildDataForm, ParentDataForm



# Create your views here.

class ParentIndexView(generic.TemplateView):
    template_name = 'parent/index.html'

    def get_context_data(self, *args, **kwargs):
        context = {'teacher_id': self.request.resolver_match.kwargs['teacher_id']}
        return context


class ConsentView(generic.TemplateView):
    template_name = 'parent/consent.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'teacher_id': self.request.resolver_match.kwargs['teacher_id'],
            'status_text': StatusData.objects.filter(
                status_number=self.request.resolver_match.kwargs['status_number'])
        }
        return context


class ChildView(generic.TemplateView):
    template_name = 'parent/child.html'

    def get_context_data(self, *args, **kwargs):
        teacher_id = self.request.resolver_match.kwargs['teacher_id']
        teacher = TeacherData.objects.get(teacher_id=teacher_id)
        child = ChildData.objects.create(teacher_id=teacher_id)
        child_id = child.child_id
        context = {
            'teacher_id': teacher_id,
            'child_id': child_id,
            'form': ChildDataForm(),
            'status_text': StatusData.objects.filter(
                status_number=self.request.resolver_match.kwargs['status_number'])
        }
        return context


def childadddata(request, **kwargs):
    child = ChildData.objects.filter(
        child_id=kwargs['child_id']
    )[0]

    for field_name, field_data in request.POST.items():
        try:
            setattr(child, field_name, field_data)
        except:
            pass
    child.save()

    child_id = child.child_id
    return HttpResponseRedirect(reverse('parent:parent', args=[child_id, 0]))


class ParentView(generic.TemplateView):
    template_name = 'parent/parent.html'

    def get_context_data(self, *args, **kwargs):
        child_id = self.request.resolver_match.kwargs['child_id']
        parent = ParentData.objects.create(child_id=child_id)
        parent_id = parent.parent_id
        context = {
            'child_id': child_id,
            'parent_id': parent_id,
            'form': ParentDataForm(),
            'status_text': StatusData.objects.filter(
                status_number=self.request.resolver_match.kwargs['status_number'])
        }
        return context


def parentadddata(request, **kwargs):
    parent = ParentData.objects.filter(
        parent_id=kwargs['parent_id']
    )[0]

    for field_name, field_data in request.POST.items():
        try:
            setattr(parent, field_name, field_data)
        except:
            pass
    parent.save()

    return HttpResponseRedirect(reverse('questionnaire:explanation', args=["parent", parent.parent_id,
                                                                           "parent", parent.parent_id]))


def childquestionnaire(request, **kwargs):
    parent = ParentData.objects.filter(
        parent_id=kwargs['parent_id']
    )[0]
    parent_id = parent.parent_id
    child_id = parent.child_id

    child = ChildData.objects.get(child_id=child_id)
    setattr(child, 'parent_q', True)
    child.save()

    return HttpResponseRedirect(reverse('questionnaire:explanation', args=["parent", parent_id,
                                                                           "child", parent.child_id]))


class ChildselfquestionnaireView(generic.TemplateView):
    template_name = 'parent/childselfquestionnaire.html'

    def get_context_data(self, *args, **kwargs):
        parent_id = self.request.resolver_match.kwargs['parent_id']
        context = { 'parent_id': parent_id}
        return context


def gotochildself(request, **kwargs):
    parent = ParentData.objects.filter(
        parent_id=kwargs['parent_id']
    )[0]
    child_id = parent.child_id

    return HttpResponseRedirect(reverse('questionnaire:explanation', args=["child", child_id,
                                                                           "child", child_id]))


class ThankyouView1(generic.TemplateView):
    template_name = 'parent/thankyou.html'

    def get_context_data(self, *args, **kwargs):
        parent_id = self.request.resolver_match.kwargs['parent_id']
        parent = ParentData.objects.get(parent_id=parent_id)
        child_id = parent.child_id

        child = ChildData.objects.get(child_id=child_id)
        setattr(child, 'child_q', True)
        child.save()

        context = {
            'parent_id': parent_id
        }
        return context


class ThankyouView1(generic.TemplateView):
    template_name = 'parent/thankyou.html'

    def get_context_data(self, *args, **kwargs):
        parent_id = self.request.resolver_match.kwargs['parent_id']
        parent = ParentData.objects.get(parent_id=parent_id)
        child_id = parent.child_id

        child = ChildData.objects.get(child_id=child_id)
        setattr(child, 'child_q', True)
        child.save()

        context = {
            'parent_id': parent_id
        }
        return context



class ThankyouView2(generic.TemplateView):
    template_name = 'parent/thankyou.html'

    def get_context_data(self, *args, **kwargs):
        child_id = self.request.resolver_match.kwargs['child_id']

        child = ChildData.objects.get(child_id=child_id)
        setattr(child, 'self_q', True)
        child.save()

        context = {
            'parent_id': child_id
        }
        return context
