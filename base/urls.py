from django import views
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView
from base import views

urlpatterns = [
  path('', TaskList.as_view(), name='tasks'),
  path('task/<int:pk>', TaskDetail.as_view(), name='task'),
  path('task-create/', TaskCreate.as_view(), name='task-create'),
  path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
  path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]