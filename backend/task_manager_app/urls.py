from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Other URL patterns...
    path('admin/', admin.site.urls),
    path('task_manager/', include('task_manager_app.urls')),
]