from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/new/', views.task_form, name='task_form'),
    path('create/', views.task_create, name='task_create'),
    path('<int:id>/edit/', views.task_update, name='task_update'),
    path('<int:id>/confirm_delete/', views.confirm_delete, name='confirm_delete'),
    path('<int:id>/delete/', views.task_delete, name='task_delete'),
]