from django.forms import ModelForm
from .models import ChildData, ParentData


class ChildDataForm(ModelForm):
    class Meta:
        model = ChildData
        fields = ['name_text', 'gender', 'dob']


class ParentDataForm(ModelForm):
    class Meta:
        model = ParentData
        fields = ['name_text', 'email', 'gender', 'age']