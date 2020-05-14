from django.shortcuts import render
from django.views import generic
from .models import TeacherData
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render


# Create your views here.

# landing page
class IndexView(generic.TemplateView):
    # template_name = 'teacher/index.html'
    template_name = 'teacher/test.html'
    context_object_name = 'teacher_index'


class LoginView(generic.ListView):
    template_name = 'teacher/login.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return "teacher login"


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    print('add user')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('teacher:detail'))
    else:
        print('invalid')
        # Return an 'invalid login' error message.


class DetailView(generic.TemplateView):
    template_name = 'teacher/detail.html'


def update(request):
    model = TeacherData
    teacher = model.objects.create(
        username = request.POST['username'],
        password = request.POST['password'],
        name_text = request.POST['name']
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

