from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceForm(forms.ModelForm):
    choices = [(1, '왼쪽'), (2, '오른쪽')]
    pick = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    class Meta:
        model = Choice
        fields = ('pick', 'comment',)