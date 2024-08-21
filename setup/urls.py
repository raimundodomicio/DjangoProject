from django.contrib import admin
from django.urls import path

from tasks.views import tasks_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tasks_list),
]
