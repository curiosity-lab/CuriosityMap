from django.shortcuts import render
from django.views import generic
from .models import TeacherData, StatusData
from parent.models import ChildData
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .forms import TeacherDataForm

# Create your views here.


# landing page
class TeacherIndexView(generic.TemplateView):
    template_name = 'teacher/index.html'
    context_object_name = 'teacher_index'


class RegisterView(generic.ListView):
    model = StatusData
    template_name = 'teacher/register.html'
    context_object_name = 'details'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return StatusData.objects.filter(
            status_number=self.request.resolver_match.kwargs['status_number']
        )


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('teacher:children', args=[TeacherData.objects.filter(
            username=username
        )[0].teacher_id]))
    else:
        return HttpResponseRedirect(reverse('teacher:register', args=[20]))
        # Return an 'invalid login' error message.


def update(request):
    model = TeacherData

    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username=username, password=password)
    except:
        return HttpResponseRedirect(reverse('teacher:register', args=[20]))


    teacher = model.objects.create(
        username = username,
        password = password,
    )

    form = TeacherDataForm()

    return render(request, 'teacher\detail.html', {'form': form, 'teacher_id': teacher.teacher_id})
    # return HttpResponseRedirect(reverse(render(request, 'teacher\consent.html', {'form': form}), args=["teacher.teacher_id]))
    #
    # return HttpResponseRedirect(reverse('questionnaire:explanation', args=["teacher", teacher.teacher_id,
    #                                                                        "teacher", teacher.teacher_id]))


def adddata(request, **kwargs):
    teacher = TeacherData.objects.filter(
        teacher_id=kwargs['teacher_id']
    )[0]

    for field_name, field_data in request.POST.items():
        try:
            setattr(teacher, field_name, field_data)
            # teacher[field_name] = field_data
        except:
            pass
    teacher.save()

    return HttpResponseRedirect(reverse('questionnaire:explanation', args=["teacher", teacher.teacher_id,
                                                                           "teacher", teacher.teacher_id]))

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


class TeacherView(generic.ListView):
    template_name = 'teacher/teacher.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return "teacher data"


class ChildrenView(generic.ListView):
    template_name = 'teacher/children.html'
    context_object_name = 'children'

    def get_queryset(self):
        """
        Get all children associated with teacher id:
        teacher.teacher_id = parent.teacher_id AND
        parent.child_id = parent.child_id AND
        parent.consent = True
        """
        teacher_id = self.request.resolver_match.kwargs['teacher_id']
        the_children = ChildData.objects.filter(teacher_id=teacher_id)

        context = {
            'teacher_id': teacher_id,
            'children': the_children
        }
        return context


def childquestionnaire(request, **kwargs):
    teacher_id = kwargs['teacher_id']
    child_id = kwargs['child_id']

    child = ChildData.objects.get(child_id=child_id)
    setattr(child, 'teacher_q', True)
    child.save()

    return HttpResponseRedirect(reverse('questionnaire:explanation', args=["teacher", teacher_id,
                                                                           "child", child_id]))
