from django.contrib import admin
from django.urls import path
from todo_app import views

urlpatterns=[
    path('',views.index , name='index'),
    path('update/<str:pk>', views.updateTask,name='updateTask'),
    path('delete/<str:pk>',views.deleteTask,name='deleteTask')
]