from django.contrib import admin
from .models import TodosModel, ContactModel

admin.site.register(TodosModel)
admin.site.register(ContactModel)
