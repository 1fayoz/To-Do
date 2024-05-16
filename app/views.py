from django.shortcuts import render
from .models import Task
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView

def home(request):
    task = Task.objects.all()
    return render(request, 'index.html', {'task': task})

def CreateTask(request):
    if request.method == 'POST':
        print(request.POST)
        task = request.POST.get('task')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')

        Task.objects.create(
               title = task,
               discription = description,
                deadline = deadline
        )
        return HttpResponseRedirect('/')
    return render(request, 'create_task.html')

def EditTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        task.status = status
        task.save()
        return HttpResponseRedirect('/')
    
    return render (request, 'edit_task.html', {'task':task})

def delete_model(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect('/')
    return render(request, 'index.html' )



class Taskserializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'discription',)



class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = Taskserializer






