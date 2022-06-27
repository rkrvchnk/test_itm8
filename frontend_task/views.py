from django.shortcuts import render


class Counter:
    count = 0



rollups_clicks = Counter()


def index(request):
    return render(request, 'frontend_task/index.html', {})


def rollups(request):

    rollups_clicks.count += 1
    return render(request, 'frontend_task/rollups.html', {'count': rollups_clicks.count})
