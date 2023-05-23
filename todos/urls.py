from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('create/', create, name='create'),
    path('delete/<int:todos_id>', delete, name='delete'),
    path('update/<int:todos_id>', update, name='update'),
    path('toggle-completed/<int:todos_id>/',
         toggle_completed, name='toggle_completed'),

]
