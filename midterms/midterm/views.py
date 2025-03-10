from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def task(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def save(request):
        title = request.POST['title']
        description = request.POST['description']
        assigned_personnel = request.POST['assigned_personnel']
        due_date = request.POST['due_date']
        status = request.POST['status']

        newTask = Task(title = title, description = description, assigned_personnel = assigned_personnel, due_date = due_date, status = status)
        newTask.save()
                
        return redirect('/midterm/task')

def edit(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task_form.html', {'task': task})

def update(request, id):
    task = Task.objects.get(id=id)
    task.title = request.POST['title']
    task.description = request.POST['description']
    task.assigned_personnel = request.POST['assigned_personnel']
    task.due_date = request.POST['due_date']
    task.status = request.POST['status']
    task.save()

    task = Task.objects.all()
    return redirect('/midterm/task')

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/midterm/task')



