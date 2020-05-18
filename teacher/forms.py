from django.forms import ModelForm
from .models import TeacherData


class TeacherDataForm(ModelForm):
    class Meta:
        model = TeacherData
        fields = ['name_text', 'gender', 'age', 'city_text', 'school_text', 'teacher_type', 'grade', 'topic']