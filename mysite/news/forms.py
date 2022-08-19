import re

from django import forms
from django.core.exceptions import ValidationError

from .models import News, Category
from captcha.fields import CaptchaField


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control",
#                                                                            "rows": 10 }))
#     is_published = forms.BooleanField(initial=True, widget=forms.CheckboxInput(attrs={
#         "class": "form-check-input"
#     }))
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, widget=forms.Select(attrs={
#         "class": "form-control"
#     }))


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = None

    # category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, widget=forms.Select(attrs={
    #         "class": "form-control"}))

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Name must not start with a number')
        return title

    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control",
                                             "rows": 10}),
            'is_published': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'category': forms.Select(attrs={"class": "form-control"})

        }


class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField()

    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if re.match(r'\d', subject):
            raise ValidationError('Name must not start with a number')
        return subject