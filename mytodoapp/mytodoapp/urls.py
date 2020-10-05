from django.contrib import admin
from django.urls import path, re_path

from todo.views import index, add_todo, delete_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    re_path(r'add_todo/', add_todo),
    path('delete_todo/<int:todo_id>/', delete_todo),
]
