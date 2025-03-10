from django.urls import path
from . import views

urlpatterns = [
    path('task', views.task, name='task'),
    path('save', views.save, name='save'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('edit/<int:id>/update/', views.update, name='update'),
    path('delete/<int:id>/', views.delete),
]