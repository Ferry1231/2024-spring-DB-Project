# forms.py

from django import forms
from .models import Grade

class CourseSelectionForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['stu_id', 'cous_id']
