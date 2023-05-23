from django.shortcuts import render, redirect, get_object_or_404
from .models import TodosModel
from .forms import ListForm


def index(request):
    todo_list = TodosModel.objects.all()
    return render(request, 'todos/index.html', {'todo_list': todo_list})


def contact(request):
    return render(request, 'todos/contact.html')


def create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'todos/create.html')


def delete(request, todos_id):
    todo = TodosModel.objects.get(pk=todos_id)
    todo.delete()
    return redirect('index')


def update(request, todos_id):
    todo = TodosModel.objects.get(pk=todos_id)

    if request.method == 'POST':
        form = ListForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ListForm(instance=todo)

    return render(request, 'todos/update.html', {'form': form})
