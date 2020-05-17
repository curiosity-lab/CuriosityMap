from django.shortcuts import render
from django.views import generic
from .models import TeacherData, StatusData
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User


# Create your views here.

# landing page
class IndexView(generic.TemplateView):
    template_name = 'teacher/index.html'
    context_object_name = 'teacher_index'


def register(request):

    print('add user')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('teacher:children'))
    else:
        return HttpResponseRedirect(reverse('teacher:detail', args=[20]))
        # Return an 'invalid login' error message.


class DetailView(generic.ListView):
    model = StatusData
    template_name = 'teacher/detail.html'
    context_object_name = 'details'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return StatusData.objects.filter(
            status_number=self.request.resolver_match.kwargs['status_number']
        )

def update(request):
    model = TeacherData

    username = request.POST['username']
    password = request.POST['password']
    fullname = request.POST['fullname']
    try:
        user = User.objects.create_user(username, fullname, password)
    except:
        return HttpResponseRedirect(reverse('teacher:detail', args=[20]))


    teacher = model.objects.create(
        username = username,
        password = password,
        name_text = fullname
    )

    return HttpResponseRedirect(reverse('questionnaire:explanation', args=["teacher", teacher.teacher_id,
                                                                           "teacher", teacher.teacher_id]))


class TeacherView(generic.ListView):
    template_name = 'teacher/teacher.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return "teacher data"


# TODO
class ChildrenView(generic.ListView):
    template_name = 'teacher/children.html'

    def get_queryset(self):
        """
        Get all children associated with teacher id:
        teacher.teacher_id = child.teacher_id AND
        child.child_id = parent.child_id AND
        parent.consent = True
        """

        return "teacher login"

