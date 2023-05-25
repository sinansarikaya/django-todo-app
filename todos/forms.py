from django import forms
from .models import Todo, Contact


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        help_text="Enter the title of your todo item.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label="Content",
        help_text="Enter the content of your todo item.",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    is_completed = forms.BooleanField(
        label="Is completed",
        help_text="Check this box if the item is completed.",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Todo
        fields = ['title', 'content', 'is_completed']

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        help_text="Enter your name.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        help_text="Enter your email address.",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label="Message",
        help_text="Enter your message.",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
