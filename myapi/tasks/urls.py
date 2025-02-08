from django.urls import path
from django.views.generic import RedirectView
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('', RedirectView.as_view(url='tasks/')),
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
