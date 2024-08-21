from django.shortcuts import render

from .models import Task

# Create your views here.


def tasks_list(request):
    task = Task.objects.all()
    return render(request, "task/tasks_list.html", {"task": task})
