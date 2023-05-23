from django import forms
from .models import TodosModel


class ListForm(forms.ModelForm):
    class Meta:
        model = TodosModel
        fields = ['title', 'content']
