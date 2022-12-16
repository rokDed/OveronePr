from django import forms
from django.forms import ModelForm
from . models import *
from django.contrib.admin import widgets

class work_plan_Forms(forms.ModelForm):
    class Meta:
        model = work_plan
        fields = '__all__'

