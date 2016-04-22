from django import forms

from registry.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'birthday', 'year', 'house', 'wand']
