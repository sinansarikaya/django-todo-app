from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TodosModel
from .forms import ListForm


def index(request):
    todo_list = TodosModel.objects.order_by('-updated_at')
    return render(request, 'todos/index.html', {'todo_list': todo_list})


def contact(request):
    return render(request, 'todos/contact.html')


def create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo item successfully added!')
            return redirect('index')
        else:
            messages.error(request, 'Error adding todo item. Please try again.')
    else:
        return render(request, 'todos/create.html')


def delete(request, todos_id):
    try:
        todo = get_object_or_404(TodosModel, pk=todos_id)
        todo.delete()
        messages.warning(request, 'The deletion process was completed successfully.')
    except Exception as e:    
        messages.error(request, 'Error deleting todo item. Please try again.')
    return redirect('index')


def update(request, todos_id):
    todo = TodosModel.objects.get(pk=todos_id)

    if request.method == 'POST':
        form = ListForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo item successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Error updating todo item. Please try again.')
    else:
        form = ListForm(instance=todo)

    return render(request, 'todos/update.html', {'form': form})


def toggle_completed(request, todos_id):
    todo = get_object_or_404(TodosModel, pk=todos_id)
    todo.is_completed = not todo.is_completed
    todo.save()

    if todo.is_completed:
        messages.success(request, 'Task marked as completed!')
    else:
        messages.warning(request, 'Task marked as incomplete!')
    
    return redirect('index')
