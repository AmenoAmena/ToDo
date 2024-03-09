from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('tasks',views.task_list,name = 'tasks'),
    path('delete<int:id>',views.delete,name = 'delete')
]