from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('frontend_task.urls')),
    path('rollups/', include('frontend_task.urls')),
    path('admin/', admin.site.urls),
]
