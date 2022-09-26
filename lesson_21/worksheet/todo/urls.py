from django.urls import path, include
from .views import TodoListView
from .services import add_Item, delete_item


urlpatterns = [
    path('', TodoListView.as_view(), name='task_list'),
    path('add/', add_Item, name='add_task'),
    path('delete/<int:object>', delete_item, name='delete_task'),

]