from django.shortcuts import render
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(task = task )
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'ToDoApp/index.html',{
        'tasks':tasks,
        'form':form  
    })