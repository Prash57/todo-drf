from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todos'),
    path('update-task/<str:pk>/', views.updateTask, name='update'),
    path('delete-task/<str:pk>/', views.deleteTask, name='delete'),

]
