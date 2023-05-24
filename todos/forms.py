from django import forms
from .models import TodosModel, ContactModel


class ListForm(forms.ModelForm):
    class Meta:
        model = TodosModel
        fields = ['title', 'content', 'is_completed']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
