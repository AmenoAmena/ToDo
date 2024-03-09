from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = TaskForm()
        else:
            task = Task.objects.get(pk=id)
            form = TaskForm(instance=task)
        return render(request, 'ToDoApp/index.html',{
            'form':form  
        })
    else:
        if id==0:
            form = TaskForm(request.POST)
        else:
            task = Task.objects.get(pk=id)
            form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks')


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'ToDoApp/task_list.html',{
        'tasks':tasks
    })

def delete(request,id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('tasks')