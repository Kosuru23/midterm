from django.shortcuts import render, redirect
from datetime import date
from .models import Task

# Create your views here.

# Show the list of task in task_list.html
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

# Open the task_form.html to create the task
def task_form(request):
    return render(request, 'task_form.html')

# Create the task in task_form.html
def task_create(request):
    
    title = request.POST['title']
    description = request.POST['description']
    due_date = request.POST['due_date']

    due_date = date.fromisoformat(due_date)
    today = date.today()
    if due_date < today:
        status = "Overdue"
    elif due_date == today:
        status = "Due Today"
    else:
        status = "Upcoming"

    newTask = Task(title = title, description = description, due_date = due_date, status=status)
    newTask.save()
            
    return redirect('/midterm/')

# Update / Edit the task in task_form.html
def task_update(request, id):
    task = Task.objects.get(id=id)  # Get task or return 404 if not found

    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']

        task.due_date = date.fromisoformat(task.due_date)
        today = date.today()
        
        if task.due_date < today:
            task.status = "Overdue"
        elif task.due_date == today:
            task.status = "Due Today"
        else:
            task.status = "Upcoming"

        task.save()  # Save the updates
        return redirect('/midterm/')  # Redirect back to task list

    return render(request, 'task_form.html', {'task': task})  # Show form with existing data

# Opens the task_confirm_delete.html to ask the user to confirm deletion
def confirm_delete(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task_confirm_delete.html', {'task': task})

# Deletes the task
def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/midterm/')


    



