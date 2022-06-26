from django.urls import path

from . import views

app_name = 'frontend_task'

urlpatterns = [
    path('', views.index, name='index'),
    path('rollups/', views.rollups, name='rollups'),
]
