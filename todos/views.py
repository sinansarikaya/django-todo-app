from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo
from .forms import TodoForm, ContactForm


def index(request):
    todo_list = Todo.objects.order_by('-updated_at')
    return render(request, 'todos/index.html', {'todo_list': todo_list})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Error sending the message. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'todos/contact.html', {'form': form})

@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)  
            todo.user = request.user  
            todo.save()  
            messages.success(request, 'Todo item successfully added!')
            return redirect('index')
        else:
            if 'title' in form.errors:
                messages.error(request, 'Error with the title field. Please try again.')
            if 'content' in form.errors:
                messages.error(request, 'Error with the content field. Please try again.')
    else:
        form = TodoForm()

    return render(request, 'todos/create.html', {'form': form})


@login_required
def delete(request, todos_id):
    try:
        todo = get_object_or_404(Todo, pk=todos_id)
        todo.delete()
        messages.warning(request, 'The deletion process was completed successfully.')
    except Exception as e:    
        messages.error(request, 'Error deleting todo item. Please try again.')
    return redirect('index')

@login_required
def update(request, todos_id):
    todo = Todo.objects.get(pk=todos_id)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo item successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Error updating todo item. Please try again.')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todos/update.html', {'form': form})

@login_required
def toggle_completed(request, todos_id):
    todo = get_object_or_404(Todo, pk=todos_id)
    todo.is_completed = not todo.is_completed
    todo.save()

    if todo.is_completed:
        messages.success(request, 'Task marked as completed!')
    else:
        messages.warning(request, 'Task marked as incomplete!')
    
    return redirect('index')
