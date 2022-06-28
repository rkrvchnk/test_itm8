from django.shortcuts import render


def index(request):
    return render(request, 'frontend_task/index.html', {})


def rollups(request):
    return render(request, 'frontend_task/rollups.html', {})
