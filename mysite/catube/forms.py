from django import forms
from catube.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # widgets = {
        #     'subject':forms.TextInput(attrs={'class': 'form-control'}),
        #     'content':forms.Textarea(attrs={'class': 'form-control', 'row': 10}),
        #
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields= ['content']
        labels = {'content': '답변내용'}

