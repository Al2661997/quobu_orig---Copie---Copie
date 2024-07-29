from django import forms
from django.forms import ModelForm
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'




    
    