from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(task = task )
        return redirect('tasks') 
    form = TaskForm()
    return render(request, 'ToDoApp/index.html',{
        'form':form  
    })

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'ToDoApp/task_list.html',{
        'tasks':tasks
    })